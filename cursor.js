// Custom cursor — dot + lagging ring
(function () {
  const dot  = document.createElement('div');
  const ring = document.createElement('div');
  dot.className  = 'cursor-dot';
  ring.className = 'cursor-ring';
  document.body.appendChild(dot);
  document.body.appendChild(ring);

  let mX = 0, mY = 0;
  let rX = 0, rY = 0;

  const lerp = (a, b, t) => a + (b - a) * t;

  document.addEventListener('mousemove', (e) => {
    mX = e.clientX; mY = e.clientY;
    dot.style.left = mX + 'px';
    dot.style.top  = mY + 'px';
    if (!dot.classList.contains('visible')) {
      dot.classList.add('visible');
      ring.classList.add('visible');
    }
  });

  (function tick() {
    rX = lerp(rX, mX, 0.1);
    rY = lerp(rY, mY, 0.1);
    ring.style.left = rX + 'px';
    ring.style.top  = rY + 'px';
    requestAnimationFrame(tick);
  })();

  document.addEventListener('mouseleave', () => {
    dot.style.opacity  = '0';
    ring.style.opacity = '0';
  });
  document.addEventListener('mouseenter', () => {
    dot.style.opacity  = '';
    ring.style.opacity = '';
  });

  document.addEventListener('mousedown', () => ring.classList.add('is-clicking'));
  document.addEventListener('mouseup',   () => ring.classList.remove('is-clicking'));

  document.addEventListener('mouseover', (e) => {
    if (e.target.closest('a, button, .card')) {
      dot.classList.add('is-hovering');
      ring.classList.add('is-hovering');
    }
  });
  document.addEventListener('mouseout', (e) => {
    if (e.target.closest('a, button, .card')) {
      dot.classList.remove('is-hovering');
      ring.classList.remove('is-hovering');
    }
  });
})();
