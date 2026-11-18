// Service worker: rende il gioco installabile e giocabile anche senza internet.
// La pagina usa "prima la rete": se c'è connessione si scarica sempre la versione nuova.
// Cambia VERSION quando aggiungi file da tenere in cache.
const VERSION = 'rissa-v1';
const CORE = ['./', './index.html', './manifest.webmanifest', './assets/icon-192.png', './assets/icon-512.png', './assets/favicon-32.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  const isFont = url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com';
  if (req.mode === 'navigate' || (url.origin === location.origin && !isFont)) {
    // prima la rete, poi la cache
    e.respondWith(fetch(req).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy)); }
      return res;
    }).catch(() => caches.match(req).then(r => r || caches.match('./index.html'))));
  } else if (isFont) {
    // font: prima la cache
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => {
      const copy = res.clone(); caches.open(VERSION).then(c => c.put(req, copy)); return res;
    })));
  }
});
