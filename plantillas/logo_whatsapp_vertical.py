"""Logo animado vertical + número de WhatsApp que entra abajo con un "pop".
Uso: python3 -I plantillas/logo_whatsapp_vertical.py   -> marca/logo-lancarg-animado-vertical-whatsapp.mp4
Momento del "pop" (para poner el sonido en la edición): T0 = 3.0 s.
"""
import math, os, subprocess, tempfile
from playwright.sync_api import sync_playwright

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "marca", "logo-lancarg-animado-vertical.mp4")
OUT = os.path.join(ROOT, "marca", "logo-lancarg-animado-vertical-whatsapp.mp4")
FPS, T0, TOTAL = 30, 3.0, 7.0
WA = ('<svg viewBox="0 0 24 24" width="70" height="70" fill="#fff"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg>')
HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;background:transparent;width:1080px;height:1920px;overflow:hidden;font-family:Inter,sans-serif}}
#wrap{{position:absolute;left:0;right:0;top:1330px;display:flex;flex-direction:column;align-items:center}}
#pill{{display:flex;align-items:center;gap:30px;background:#02462D;border-radius:999px;padding:26px 56px 26px 26px;
  box-shadow:0 24px 50px rgba(2,70,45,.28);position:relative;overflow:hidden}}
#ic{{width:116px;height:116px;border-radius:50%;background:#25D366;display:flex;align-items:center;justify-content:center;flex:none}}
#tx{{color:#fff;line-height:1.05}}
#tx small{{display:block;font-size:34px;font-weight:600;opacity:.9;letter-spacing:.02em}}
#tx b{{display:block;font-size:76px;font-weight:900;letter-spacing:-.01em}}
#shine{{position:absolute;top:-20%;bottom:-20%;width:120px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-20deg)}}
#line{{height:6px;background:#E70A0F;border-radius:3px;margin-top:40px}}
</style></head><body><div id="wrap"><div id="pill"><div id="ic">{WA}</div>
<div id="tx"><small>Escribinos por WhatsApp</small><b>264 454-3612</b></div><div id="shine"></div></div><div id="line"></div></div></body></html>"""


def back(p, s=1.9):  # easeOutBack: pasa un poquito y vuelve (efecto "pop")
    p -= 1
    return 1 + (s + 1) * p ** 3 + s * p ** 2


def clamp(x): return max(0.0, min(1.0, x))


def state(t):
    d = t - T0
    p = clamp(d / 0.55)
    e = back(p) if p < 1 else 1
    op = clamp(d / 0.2)
    y = (1 - e) * 220
    sc = 0.55 + 0.45 * e
    # ícono: aparece con rebote un poco después y "suena" (vibra) dos veces
    pi = clamp((d - 0.25) / 0.45)
    isc = back(pi, 2.6) if pi < 1 else 1
    rot = 0
    if 0.9 < d < 1.5:
        rot = 14 * math.sin((d - 0.9) * 2 * math.pi * 5) * (1 - (d - 0.9) / 0.6)
    sx = -200 + clamp((d - 0.7) / 0.7) * 1100  # brillo que cruza la píldora
    lw = 220 * (1 - (1 - clamp((d - 0.45) / 0.5)) ** 3)  # línea roja que se dibuja
    return op, y, sc, isc, rot, sx, lw


def main():
    tmp = tempfile.mkdtemp(dir=os.environ.get("TMPDIR"))
    n = int(TOTAL * FPS)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.set_content(HTML); pg.wait_for_timeout(300)
        for i in range(n):
            t = i / FPS
            op, y, sc, isc, rot, sx, lw = state(t)
            pg.evaluate(f"""()=>{{const w=document.getElementById('wrap');w.style.opacity={op};
              document.getElementById('pill').style.transform='translateY({y:.1f}px) scale({sc:.4f})';
              document.getElementById('ic').style.transform='scale({isc:.4f}) rotate({rot:.2f}deg)';
              document.getElementById('shine').style.left='{sx:.1f}px';
              document.getElementById('line').style.width='{lw:.1f}px';}}""")
            pg.screenshot(path=os.path.join(tmp, f"f{i:04d}.png"), omit_background=True)
        b.close()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-framerate", str(FPS), "-i", os.path.join(tmp, "f%04d.png"),
                    "-filter_complex", f"[0:v]tpad=stop_mode=clone:stop_duration={TOTAL}[bg];[bg][1:v]overlay=0:0:shortest=1,format=yuv420p",
                    "-t", str(TOTAL), "-r", str(FPS), "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-movflags", "+faststart", OUT], check=True)
    print(OUT)


if __name__ == "__main__":
    main()
