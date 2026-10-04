// Offline-Test des Workers: Verschlüsselung gegen die Vektoren aus RFC 8291 Anhang A, Entschlüsselung einer
// zufälligen Nachricht mit dem Schlüssel des Empfängers, VAPID-Signatur, HTTP-Pfade und der stündliche Lauf mit
// einem KV-Ersatz im Speicher.   Aufruf: node push/test.mjs
import { encrypt, vapidHeader, handle, erinnern, lokal, b64u } from './src/worker.js';

let fails = 0;
const check = (ok, msg) => { if (!ok) { fails++; console.log('FEHLER', msg); } };
const te = new TextEncoder(), td = new TextDecoder();

// RFC 8291 Anhang A
const V = {
  plaintext: 'V2hlbiBJIGdyb3cgdXAsIEkgd2FudCB0byBiZSBhIHdhdGVybWVsb24',
  asPublic: 'BP4z9KsN6nGRTbVYI_c7VJSPQTBtkgcy27mlmlMoZIIgDll6e3vCYLocInmYWAmS6TlzAC8wEqKK6PBru3jl7A8',
  asPrivate: 'yfWPiYE-n46HLnH0KqZOF1fJJU3MYrct3AELtAQ-oRw',
  uaPublic: 'BCVxsr7N_eNgVRqvHtD0zTZsEc6-VV-JvLexhqUzORcxaOzi6-AYWXvTBHm4bjyPjs7Vd8pZGH6SRpkNtoIAiw4',
  uaPrivate: 'q1dXpw3UpT5VOmu_cf_v6ih07Aems3njxI-JWgLcM94',
  salt: 'DGv6ra1nlYgDCS1FRnbzlw',
  auth: 'BTBZMqHH6r4Tts7J_aSIgg',
  header: 'DGv6ra1nlYgDCS1FRnbzlwAAEABBBP4z9KsN6nGRTbVYI_c7VJSPQTBtkgcy27mlmlMoZIIgDll6e3vCYLocInmYWAmS6TlzAC8wEqKK6PBru3jl7A8',
  ciphertext: '8pfeW0KbunFT06SuDKoJH9Ql87S1QUrdirN6GcG7sFz1y1sqLgVi1VhjVkHsUoEsbI_0LpXMuGvnzQ',
};
const keyPair = async (pub, priv, usage) => {
  const p = b64u.dec(pub);
  const jwk = { kty: 'EC', crv: 'P-256', x: b64u.enc(p.slice(1, 33)), y: b64u.enc(p.slice(33, 65)), d: priv };
  return { publicKey: await crypto.subtle.importKey('raw', p, { name: 'ECDH', namedCurve: 'P-256' }, true, []),
           privateKey: await crypto.subtle.importKey('jwk', jwk, { name: 'ECDH', namedCurve: 'P-256' }, false, usage) };
};
const as = await keyPair(V.asPublic, V.asPrivate, ['deriveBits']);
const out = await encrypt(b64u.dec(V.uaPublic), b64u.dec(V.auth), b64u.dec(V.plaintext), { asKeyPair: as, salt: b64u.dec(V.salt) });
check(b64u.enc(out.slice(0, 86)) === V.header, 'RFC-8291-Vektor: Kopf weicht ab');
check(b64u.enc(out.slice(86)) === V.ciphertext, 'RFC-8291-Vektor: Chiffrat weicht ab');

// Entschlüsseln wie ein Browser (mit dem privaten Schlüssel des Empfängers aus dem RFC), zufälliges Salt und Serverschlüssel
async function decrypt(body, uaPriv, uaPub, auth) {
  const salt = body.slice(0, 16), asPublic = body.slice(21, 86), ct = body.slice(86);
  const ua = await keyPair(uaPub, uaPriv, ['deriveBits']);
  const asKey = await crypto.subtle.importKey('raw', asPublic, { name: 'ECDH', namedCurve: 'P-256' }, false, []);
  const ecdh = new Uint8Array(await crypto.subtle.deriveBits({ name: 'ECDH', public: asKey }, ua.privateKey, 256));
  const hkdf = async (s, ikm, info, len) => new Uint8Array(await crypto.subtle.deriveBits({ name: 'HKDF', hash: 'SHA-256', salt: s, info }, await crypto.subtle.importKey('raw', ikm, 'HKDF', false, ['deriveBits']), len * 8));
  const info = new Uint8Array([...te.encode('WebPush: info\0'), ...b64u.dec(uaPub), ...asPublic]);
  const ikm = await hkdf(b64u.dec(auth), ecdh, info, 32);
  const cek = await hkdf(salt, ikm, te.encode('Content-Encoding: aes128gcm\0'), 16);
  const nonce = await hkdf(salt, ikm, te.encode('Content-Encoding: nonce\0'), 12);
  const pt = new Uint8Array(await crypto.subtle.decrypt({ name: 'AES-GCM', iv: nonce }, await crypto.subtle.importKey('raw', cek, 'AES-GCM', false, ['decrypt']), ct));
  return td.decode(pt.slice(0, -1));
}
const msg = JSON.stringify({ title: 'Zeit für deine Fälle', body: 'Umlaute äöü' });
const rnd = await encrypt(b64u.dec(V.uaPublic), b64u.dec(V.auth), te.encode(msg));
check(await decrypt(rnd, V.uaPrivate, V.uaPublic, V.auth) === msg, 'Zufällige Nachricht lässt sich nicht entschlüsseln');

// VAPID: eigenes Schlüsselpaar, Signatur mit dem öffentlichen Schlüssel prüfen
const kp = await crypto.subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign', 'verify']);
const jwk = await crypto.subtle.exportKey('jwk', kp.privateKey);
const env = { VAPID_PUBLIC_KEY: b64u.enc(await crypto.subtle.exportKey('raw', kp.publicKey)), VAPID_PRIVATE_KEY: jwk.d, VAPID_SUBJECT: 'https://ipelico.com', ALLOW_ORIGIN: 'https://ipelico.com' };
const hdr = await vapidHeader('https://web.push.apple.com/abc', env);
const m = hdr.match(/^vapid t=([^.]+)\.([^.]+)\.([^,]+), k=(.+)$/);
check(!!m && m[4] === env.VAPID_PUBLIC_KEY, 'VAPID-Kopfzeile hat nicht die erwartete Form');
if (m) {
  const okSig = await crypto.subtle.verify({ name: 'ECDSA', hash: 'SHA-256' }, kp.publicKey, b64u.dec(m[3]), te.encode(`${m[1]}.${m[2]}`));
  const claims = JSON.parse(td.decode(b64u.dec(m[2])));
  check(okSig && claims.aud === 'https://web.push.apple.com' && claims.sub === env.VAPID_SUBJECT && claims.exp > Date.now() / 1000, 'VAPID-JWT ungültig');
}

// KV-Ersatz und HTTP-Pfade
const kv = new Map();
env.ABOS = { get: async (k, t) => kv.has(k) ? (t === 'json' ? JSON.parse(kv.get(k)) : kv.get(k)) : null, put: async (k, v) => { kv.set(k, v); }, delete: async k => { kv.delete(k); },
  list: async () => ({ keys: [...kv.keys()].map(name => ({ name })), list_complete: true }) };
const req = (method, path, body, origin = 'https://ipelico.com') => new Request('https://erinnerung.test' + path, { method, body: body === undefined ? undefined : JSON.stringify(body), headers: { 'Content-Type': 'application/json', Origin: origin } });
const sub = { endpoint: 'https://web.push.apple.com/QW5n', keys: { p256dh: V.uaPublic, auth: V.auth } };
let r = await handle(req('POST', '/abo', { sub, tz: 'Europe/Berlin', stunde: 16 }), env);
check(r.status === 200 && r.headers.get('Access-Control-Allow-Origin') === 'https://ipelico.com', 'POST /abo schlägt fehl');
r = await handle(req('POST', '/abo', { sub, tz: 'Europe/Berlin' }, 'https://boese.example'), env);
check(r.status === 403, 'Fremder Ursprung wird nicht abgewiesen');
r = await handle(req('POST', '/abo', { sub: { endpoint: 'http://x', keys: {} }, tz: 'Europe/Berlin' }), env);
check(r.status === 400, 'Ungültiges Abonnement wird angenommen');
r = await handle(req('POST', '/abo', { sub, tz: 'Mars/Olympus' }), env);
check(r.status === 400, 'Ungültige Zeitzone wird angenommen');
r = await handle(req('OPTIONS', '/abo'), env);
check(r.status === 204, 'Preflight fehlt');
check(kv.size === 1, 'Abonnement nicht gespeichert');

// Stündlicher Lauf: 16 Uhr Berlin, Ziel offen -> senden; Ziel erreicht -> nicht senden; 410 -> löschen
const at = (iso) => Date.parse(iso);
const sent = [];
const fakeFetch = status => async (url, init) => { sent.push({ url, len: init.body.length, auth: init.headers.Authorization }); return { status }; };
let s = await erinnern(env, at('2026-10-05T14:00:00Z'), fakeFetch(201)); // 16:00 MESZ
check(s.gesendet === 1 && sent.length === 1 && sent[0].len > 86 && /^vapid t=/.test(sent[0].auth), 'Erinnerung um 16 Uhr nicht gesendet');
s = await erinnern(env, at('2026-10-05T14:30:00Z'), fakeFetch(201));
check(s.gesendet === 0, 'Erinnerung am selben Tag doppelt gesendet');
s = await erinnern(env, at('2026-10-05T13:00:00Z'), fakeFetch(201));
check(s.gesendet === 0, 'Erinnerung zur falschen Stunde gesendet');
r = await handle(req('POST', '/stand', { endpoint: sub.endpoint, datum: '2026-10-06', erreicht: true }), env);
check(r.status === 200, 'POST /stand schlägt fehl');
s = await erinnern(env, at('2026-10-06T14:00:00Z'), fakeFetch(201));
check(s.gesendet === 0, 'Erinnerung trotz erreichtem Tagesziel gesendet');
s = await erinnern(env, at('2026-10-07T14:00:00Z'), fakeFetch(410));
check(s.geloescht === 1 && kv.size === 0, 'Abgelaufenes Abonnement nicht gelöscht');
r = await handle(req('POST', '/stand', { endpoint: sub.endpoint, datum: '2026-10-07', erreicht: true }), env);
check(r.status === 404, 'Stand für unbekanntes Abonnement wird angenommen');
check(lokal('Asia/Kolkata', at('2026-10-05T11:00:00Z')).stunde === 16 && lokal('America/New_York', at('2026-01-05T21:00:00Z')).stunde === 16, 'Ortszeit falsch berechnet');
check(lokal('Europe/Berlin', at('2026-10-05T23:30:00Z')).datum === '2026-10-06', 'Ortsdatum falsch berechnet');

console.log(fails ? `${fails} Fehler` : 'push/test.mjs OK');
process.exit(fails ? 1 : 0);
