// IPelico Service Worker: nur für Web Push. Kein Caching, damit die App nie veraltet ausgeliefert wird.
// Die Mitteilung um 16 Uhr schickt .github/workflows/erinnerung.yml; der Text richtet sich nach dem
// Tagesstand, den die App bei jedem Speichern unter IndexedDB ipelico/kv/heute ablegt.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));

const DAY = () => Math.floor((Date.now() - new Date().getTimezoneOffset() * 60000) / 86400000);
const heute = () => new Promise(res => {
  try {
    const o = indexedDB.open('ipelico', 1);
    o.onupgradeneeded = () => o.result.createObjectStore('kv');
    o.onsuccess = () => { const r = o.result.transaction('kv').objectStore('kv').get('heute'); r.onsuccess = () => res(r.result || null); r.onerror = () => res(null); };
    o.onerror = () => res(null);
  } catch (e) { res(null); }
});

// Safari entzieht die Berechtigung nach mehreren Pushes ohne sichtbare Mitteilung; deshalb erscheint bei erreichtem
// Tagesziel eine kurze Bestätigung statt gar nichts.
self.addEventListener('push', e => {
  e.waitUntil((async () => {
    let data = {};
    try { data = e.data ? e.data.json() : {}; } catch (_) { data = { body: e.data ? e.data.text() : '' }; }
    const st = await heute();
    const goal = (st && st.goal) || 100;
    const x = st && st.d === DAY() ? st.x : 0;
    let title, body;
    if (x >= goal) {
      title = 'Tagesziel geschafft';
      body = `Streak gesichert${st.streak ? ` – ${st.streak} ${st.streak === 1 ? 'Tag' : 'Tage'}` : ''}. Bis morgen!`;
    } else {
      title = data.title || 'Zeit für deine Fälle';
      body = x ? `Noch ${goal - x} XP bis zum Tagesziel – etwa ${Math.ceil((goal - x) / 10)} Fälle.`
               : (data.body || `Heute noch keine Fälle gelöst. ${goal} XP sichern den Streak.`);
    }
    await self.registration.showNotification(title, { body, icon: 'icon-192.png', badge: 'icon-192.png', tag: 'ipelico-tagesziel', data: { url: './#/' } });
  })());
});

self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(cs => {
    const c = cs.find(c => 'focus' in c);
    return c ? c.focus() : self.clients.openWindow('./');
  }));
});
