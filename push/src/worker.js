// IPelico Erinnerung: Cloudflare Worker, der Push-Abonnements verwaltet und stündlich die Geräte anstößt,
// bei denen gerade die gewählte Erinnerungsstunde ist und das Tagesziel noch offen ist.
// Gespeichert wird je Gerät nur: Push-Adresse und -Schlüssel des Browsers, Zeitzone, Stunde, Datum des letzten
// erreichten Tagesziels und der letzten Erinnerung. Web Push nach RFC 8291/8292 ohne Fremdbibliothek (WebCrypto).
// Einrichtung: PLAYBOOK.md Abschnitt 14. Test: node push/test.mjs

const te = new TextEncoder();
export const b64u = {
  enc: b => btoa(String.fromCharCode(...new Uint8Array(b))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''),
  dec: s => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/') + '='.repeat((4 - s.length % 4) % 4)), c => c.charCodeAt(0)),
};
const cat = (...parts) => { const out = new Uint8Array(parts.reduce((n, p) => n + p.length, 0)); let o = 0; for (const p of parts) { out.set(p, o); o += p.length; } return out; };
const hkdf = async (salt, ikm, info, len) => {
  const k = await crypto.subtle.importKey('raw', ikm, 'HKDF', false, ['deriveBits']);
  return new Uint8Array(await crypto.subtle.deriveBits({ name: 'HKDF', hash: 'SHA-256', salt, info }, k, len * 8));
};

// Nachricht für ein Abonnement verschlüsseln (aes128gcm). `test` erlaubt feste Schlüssel und Salt für die RFC-Vektoren.
export async function encrypt(uaPublic, auth, plaintext, test = {}) {
  const as = test.asKeyPair || await crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveBits']);
  const asPublic = new Uint8Array(await crypto.subtle.exportKey('raw', as.publicKey));
  const uaKey = await crypto.subtle.importKey('raw', uaPublic, { name: 'ECDH', namedCurve: 'P-256' }, false, []);
  const ecdh = new Uint8Array(await crypto.subtle.deriveBits({ name: 'ECDH', public: uaKey }, as.privateKey, 256));
  const ikm = await hkdf(auth, ecdh, cat(te.encode('WebPush: info\0'), uaPublic, asPublic), 32);
  const salt = test.salt || crypto.getRandomValues(new Uint8Array(16));
  const cek = await hkdf(salt, ikm, te.encode('Content-Encoding: aes128gcm\0'), 16);
  const nonce = await hkdf(salt, ikm, te.encode('Content-Encoding: nonce\0'), 12);
  const key = await crypto.subtle.importKey('raw', cek, 'AES-GCM', false, ['encrypt']);
  const ct = new Uint8Array(await crypto.subtle.encrypt({ name: 'AES-GCM', iv: nonce }, key, cat(plaintext, new Uint8Array([2]))));
  return cat(salt, new Uint8Array([0, 0, 16, 0, 65]), asPublic, ct); // Header: salt, rs = 4096, idlen = 65, as_public
}

// VAPID-Kopfzeile (RFC 8292): signiertes JWT mit dem Ursprung des Push-Dienstes als Publikum
export async function vapidHeader(endpoint, env, now = Date.now()) {
  const pub = b64u.dec(env.VAPID_PUBLIC_KEY);
  const jwk = { kty: 'EC', crv: 'P-256', x: b64u.enc(pub.slice(1, 33)), y: b64u.enc(pub.slice(33, 65)), d: env.VAPID_PRIVATE_KEY };
  const key = await crypto.subtle.importKey('jwk', jwk, { name: 'ECDSA', namedCurve: 'P-256' }, false, ['sign']);
  const h = b64u.enc(te.encode(JSON.stringify({ typ: 'JWT', alg: 'ES256' })));
  const c = b64u.enc(te.encode(JSON.stringify({ aud: new URL(endpoint).origin, exp: Math.floor(now / 1000) + 12 * 3600, sub: env.VAPID_SUBJECT })));
  const sig = await crypto.subtle.sign({ name: 'ECDSA', hash: 'SHA-256' }, key, te.encode(`${h}.${c}`));
  return `vapid t=${h}.${c}.${b64u.enc(sig)}, k=${env.VAPID_PUBLIC_KEY}`;
}

export async function send(sub, payload, env, fetchFn = fetch) {
  const body = await encrypt(b64u.dec(sub.keys.p256dh), b64u.dec(sub.keys.auth), te.encode(JSON.stringify(payload)));
  const r = await fetchFn(sub.endpoint, { method: 'POST', body,
    headers: { Authorization: await vapidHeader(sub.endpoint, env), 'Content-Encoding': 'aes128gcm', 'Content-Type': 'application/octet-stream', TTL: '3600', Urgency: 'normal', Topic: 'tagesziel' } });
  return r.status;
}

// Ortszeit eines Abonnements: Datum YYYY-MM-DD und Stunde 0–23 in seiner Zeitzone
export function lokal(tz, now = Date.now()) {
  const parts = new Intl.DateTimeFormat('en-CA', { timeZone: tz, hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit' }).formatToParts(new Date(now));
  const g = t => parts.find(p => p.type === t).value;
  return { datum: `${g('year')}-${g('month')}-${g('day')}`, stunde: +g('hour') % 24 };
}

const id = async endpoint => b64u.enc(await crypto.subtle.digest('SHA-256', te.encode(endpoint)));
const validTz = tz => { try { new Intl.DateTimeFormat('en', { timeZone: tz }); return true; } catch (e) { return false; } };
const validSub = s => { try {
  if (!s || typeof s.endpoint !== 'string' || !/^https:\/\//.test(s.endpoint) || s.endpoint.length > 2048) return false;
  const p = b64u.dec(s.keys.p256dh), a = b64u.dec(s.keys.auth);
  return p.length === 65 && p[0] === 4 && a.length === 16;
} catch (e) { return false; } };

const cors = (req, env) => {
  const origin = req.headers.get('Origin') || '';
  const allowed = (env.ALLOW_ORIGIN || '').split(',').map(s => s.trim()).filter(Boolean);
  const h = { 'Access-Control-Allow-Methods': 'GET,POST,DELETE,OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Max-Age': '86400', Vary: 'Origin' };
  if (allowed.includes(origin)) h['Access-Control-Allow-Origin'] = origin;
  return { h, ok: !origin || allowed.includes(origin) };
};
const json = (obj, status, h) => new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', ...h } });

export async function handle(req, env) {
  const { h, ok } = cors(req, env);
  if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: h });
  if (!ok) return json({ fehler: 'Ursprung nicht erlaubt' }, 403, h);
  const url = new URL(req.url);
  if (req.method === 'GET') return new Response('IPelico Erinnerung\n', { headers: { 'Content-Type': 'text/plain; charset=utf-8', ...h } });
  if ((+req.headers.get('Content-Length') || 0) > 4096) return json({ fehler: 'Anfrage zu groß' }, 413, h);
  let b; try { b = await req.json(); } catch (e) { return json({ fehler: 'Kein JSON' }, 400, h); }

  if (url.pathname === '/abo' && req.method === 'POST') {
    const stunde = Number.isInteger(b.stunde) ? b.stunde : 16;
    if (!validSub(b.sub)) return json({ fehler: 'Abonnement unvollständig' }, 400, h);
    if (typeof b.tz !== 'string' || b.tz.length > 64 || !validTz(b.tz)) return json({ fehler: 'Zeitzone unbekannt' }, 400, h);
    if (stunde < 0 || stunde > 23) return json({ fehler: 'Stunde außerhalb 0–23' }, 400, h);
    const k = await id(b.sub.endpoint);
    const alt = await env.ABOS.get(k, 'json');
    const abo = { sub: { endpoint: b.sub.endpoint, keys: { p256dh: b.sub.keys.p256dh, auth: b.sub.keys.auth } }, tz: b.tz, stunde,
      erreicht: alt ? alt.erreicht : null, gesendet: alt ? alt.gesendet : null, seit: alt ? alt.seit : new Date().toISOString().slice(0, 10) };
    await env.ABOS.put(k, JSON.stringify(abo));
    return json({ ok: true, stunde, tz: b.tz }, 200, h);
  }
  if (url.pathname === '/abo' && req.method === 'DELETE') {
    if (typeof b.endpoint !== 'string') return json({ fehler: 'endpoint fehlt' }, 400, h);
    await env.ABOS.delete(await id(b.endpoint));
    return json({ ok: true }, 200, h);
  }
  if (url.pathname === '/stand' && req.method === 'POST') {
    if (typeof b.endpoint !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(b.datum || '')) return json({ fehler: 'endpoint oder datum fehlt' }, 400, h);
    const k = await id(b.endpoint);
    const abo = await env.ABOS.get(k, 'json');
    if (!abo) return json({ ok: false, fehler: 'unbekannt' }, 404, h);
    if (b.erreicht) abo.erreicht = b.datum;
    await env.ABOS.put(k, JSON.stringify(abo));
    return json({ ok: true }, 200, h);
  }
  return json({ fehler: 'Unbekannter Pfad' }, 404, h);
}

// Stündlich: alle Abonnements durchgehen, fällige anstoßen, abgelaufene (404/410) löschen
export async function erinnern(env, now = Date.now(), fetchFn = fetch) {
  const stats = { geprueft: 0, gesendet: 0, geloescht: 0, fehler: 0 };
  const payload = { title: 'Zeit für deine Fälle', body: '100 XP sichern heute deinen Streak.' };
  let cursor;
  do {
    const page = await env.ABOS.list({ cursor, limit: 1000 });
    cursor = page.list_complete ? undefined : page.cursor;
    for (let i = 0; i < page.keys.length; i += 20) {
      await Promise.all(page.keys.slice(i, i + 20).map(async ({ name }) => {
        const abo = await env.ABOS.get(name, 'json'); if (!abo) return;
        stats.geprueft++;
        const { datum, stunde } = lokal(abo.tz, now);
        if (stunde !== abo.stunde || abo.erreicht === datum || abo.gesendet === datum) return;
        let status; try { status = await send(abo.sub, payload, env, fetchFn); } catch (e) { stats.fehler++; console.log('Push fehlgeschlagen', e.message); return; }
        if (status === 404 || status === 410) { await env.ABOS.delete(name); stats.geloescht++; return; }
        if (status >= 200 && status < 300) { abo.gesendet = datum; await env.ABOS.put(name, JSON.stringify(abo)); stats.gesendet++; }
        else { stats.fehler++; console.log('Push-Dienst antwortet', status); }
      }));
    }
  } while (cursor);
  console.log(JSON.stringify(stats));
  return stats;
}

export default {
  fetch: (req, env) => handle(req, env),
  scheduled: (event, env, ctx) => ctx.waitUntil(erinnern(env, event.scheduledTime)),
};
