// Motor de animación para reels (lo usa plantillas/render_video.py).
// En el HTML:
//   <div class="scene" data-start="0" data-end="3.4">  → escena visible de start a end (+ fundido de entrada)
//   class="bg" dentro de una escena                     → zoom suave (Ken Burns)
//   data-in="0.5"                                       → aparece subiendo, 0.5 s después de que empieza su escena
//   data-count="1957,2026" data-in="0.3" data-dur="2"   → contador de números
//   data-nologo en una escena                           → oculta el logo chico de arriba (#toplogo)
//   window.extra = (t) => {...}                         → animaciones propias de cada pieza
(function () {
  const F = 0.35; // fundido entre escenas
  const cl = x => Math.max(0, Math.min(1, x));
  window.eo = x => 1 - Math.pow(1 - cl(x), 3);
  window.cl = cl;
  const scenes = [...document.querySelectorAll('.scene')].map(el => ({
    el, a: parseFloat(el.dataset.start), b: parseFloat(el.dataset.end)
  }));
  window.DURATION = Math.max(...scenes.map(s => s.b));
  window.sceneTime = (t, id) => { const s = scenes.find(s => s.el.id === id); return t - s.a; };
  window.render = function (t) {
    let nologo = 0;
    scenes.forEach((s, i) => {
      const lt = t - s.a, d = s.b - s.a;
      // la escena anterior queda opaca debajo mientras la siguiente aparece encima
      const o = i === 0 ? 1 : cl(lt / F);
      const vis = t >= s.a && t <= s.b + F;
      s.el.style.opacity = vis ? o : 0;
      if (vis && s.el.hasAttribute('data-nologo')) nologo = Math.max(nologo, o);
      const bg = s.el.querySelector('.bg');
      if (bg) { const k = cl(lt / (d + F)); bg.style.transform = `scale(${1.04 + 0.1 * k}) translateY(${-20 * k}px)`; }
      s.el.querySelectorAll('[data-in]').forEach(n => {
        const p = eo((lt - parseFloat(n.dataset.in)) / 0.55);
        if (!n.hasAttribute('data-count')) { n.style.opacity = p; n.style.transform = `translateY(${(1 - p) * 80}px)`; }
        else {
          const [f0, f1] = n.dataset.count.split(',').map(Number), dur = parseFloat(n.dataset.dur || 2);
          const q = eo((lt - parseFloat(n.dataset.in)) / dur);
          n.textContent = Math.round(f0 + (f1 - f0) * q); n.style.opacity = cl((lt - parseFloat(n.dataset.in) + 0.3) / 0.3);
        }
      });
    });
    const tl = document.getElementById('toplogo'); if (tl) tl.style.opacity = 1 - nologo;
    if (window.extra) window.extra(t);
  };
  window.addEventListener('load', () => render(0));
})();
