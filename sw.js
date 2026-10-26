// Service Worker - 敷地＋設計雙科速刷 PWA 離線快取（2026-10-15 v8.1 改版）
// 改 APP 任何檔案後，把 CACHE_NAME 版號加一，手機才會拿到新版。
const CACHE_NAME = 'site-planning-quiz-v8.7';
const ASSETS = [
  './',
  './index.html',
  './offline_wrongbook.js',
  './tracing_lib.js',
  './reading_lib.js',
  './offline_pack.js',
  './note_hub.js',
  './nav_back.js',
  './tailwind.js',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './apple-touch-icon.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME && k !== 'site-planning-img').map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

function putCache(req, res) {
  if (res && (res.ok || res.type === 'opaque')) {
    const copy = res.clone();
    const name = /\.(webp|png|jpe?g|svg)$/i.test(new URL(req.url).pathname) ? 'site-planning-img' : CACHE_NAME;
    caches.open(name).then((c) => c.put(req, copy));
  }
  return res;
}

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;

  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req).then((res) => putCache(req, res))
        .catch(() => caches.match(req).then((r) => r || caches.match('./index.html')))
    );
    return;
  }

  e.respondWith(
    caches.match(req).then((hit) => hit || fetch(req).then((res) => putCache(req, res)))
  );
});
