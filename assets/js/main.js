// Lennart Reichow · Portfolio
// Small enhancements: nav state, mobile menu, reveal on scroll, hero video, inline videos, YouTube facade.
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var nav = document.querySelector('.site-nav');

  // Navigation background once the page is scrolled
  function updateNav() {
    if (nav) nav.classList.toggle('is-scrolled', window.scrollY > 24);
  }
  window.addEventListener('scroll', updateNav, { passive: true });
  updateNav();

  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.textContent = open ? 'Close' : 'Menu';
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        document.body.classList.remove('menu-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.textContent = 'Menu';
      });
    });
  }

  // Reveal on scroll
  var revealEls = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -6% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  // Hero video: pick a size, respect reduced motion and data saver
  var hero = document.querySelector('.hero-video');
  if (hero) {
    var saveData = navigator.connection && navigator.connection.saveData;
    if (!reduce && !saveData) {
      var small = window.innerWidth < 760;
      hero.src = small ? hero.getAttribute('data-src-small') : hero.getAttribute('data-src-large');
      hero.muted = true;
      hero.load();
      var tryPlay = function () {
        if (hero.paused && !document.hidden) {
          var p = hero.play();
          if (p && p.catch) p.catch(function () {});
        }
      };
      tryPlay();
      // Browsers pause video in background tabs, so start again once the page is looked at.
      document.addEventListener('visibilitychange', tryPlay);
      hero.addEventListener('canplay', tryPlay);
    }
  }

  // Inline videos play only while visible
  var inlineVideos = document.querySelectorAll('video.inline-video');
  if (inlineVideos.length && !reduce && 'IntersectionObserver' in window) {
    var vio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var v = entry.target;
        if (entry.isIntersecting) {
          v.muted = true;
          var pr = v.play();
          if (pr && pr.catch) pr.catch(function () {});
        } else {
          v.pause();
        }
      });
    }, { threshold: 0.35 });
    inlineVideos.forEach(function (v) { vio.observe(v); });
  }

  // YouTube: load the player only after a click
  document.querySelectorAll('.yt').forEach(function (box) {
    var btn = box.querySelector('button');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var id = box.getAttribute('data-id');
      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
      iframe.title = box.getAttribute('data-title') || 'Video';
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      iframe.setAttribute('allowfullscreen', '');
      box.innerHTML = '';
      box.appendChild(iframe);
      box.classList.add('is-playing');
    });
  });
})();
