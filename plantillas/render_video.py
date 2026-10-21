"""Renderiza una animación HTML (1080x1920) a MP4 para reels/historias.
El HTML define window.DURATION (segundos) y window.render(t), que dibuja el cuadro del segundo t.
Uso: python3 -I plantillas/render_video.py publicaciones/<carpeta>/diseno.html [salida.mp4] [--preview 1,4,8]
Con --preview solo guarda JPG de esos segundos para revisar antes de exportar.
Si el HTML define window.OVERLAY = [{src, start, x, y, w}], esos videos (ruta relativa al HTML) se superponen
al exportar desde el segundo `start` (ej. el logo animado del cierre). En --preview no aparecen."""
import sys, os, subprocess
from playwright.sync_api import sync_playwright
FPS = 30
html = os.path.abspath(sys.argv[1]); out_dir = os.path.dirname(html)
args = sys.argv[2:]
preview = None
if "--preview" in args:
    i = args.index("--preview"); preview = [float(x) for x in args[i + 1].split(",")]; del args[i:i + 2]
out = os.path.abspath(args[0]) if args else os.path.join(out_dir, "lancarg.mp4")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto("file://" + html); pg.wait_for_timeout(1000)
    stage = pg.locator("#stage")
    if preview:
        for t in preview:
            pg.evaluate(f"render({t})")
            f = os.path.join(out_dir, f"preview-{t:g}s.jpg"); stage.screenshot(path=f, type="jpeg", quality=85); print(f)
    else:
        dur = pg.evaluate("window.DURATION"); n = int(dur * FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                               "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "18",
                               "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for i in range(n):
            pg.evaluate(f"render({i / FPS})")
            ff.stdin.write(stage.screenshot(type="jpeg", quality=95))
        ff.stdin.close(); ff.wait()
        overlays = pg.evaluate("window.OVERLAY || []")
        for ov in overlays:
            src = os.path.join(out_dir, ov["src"]); tmp = out + ".tmp.mp4"
            fc = (f"[1:v]scale={ov['w']}:-2,setpts=PTS-STARTPTS+{ov['start']}/TB[ov];"
                  f"[0:v][ov]overlay={ov['x']}:{ov['y']}:eof_action=repeat")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", out, "-i", src, "-filter_complex", fc,
                            "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "18",
                            "-movflags", "+faststart", tmp], check=True)
            os.replace(tmp, out)
        print(out)
    b.close()
