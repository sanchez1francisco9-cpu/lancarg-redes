"""Renderiza cada <div class="slide" id="..."> de un HTML a JPG en la misma carpeta.
Uso: python3 plantillas/render.py publicaciones/<carpeta>/diseno.html [prefijo]
Feed: 1080x1350. Historias: 1080x1920 (definir el tamaño en el CSS de .slide)."""
import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image
html = os.path.abspath(sys.argv[1]); out = os.path.dirname(html)
prefix = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(out)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 2000})
    pg.goto("file://" + html); pg.wait_for_timeout(800)
    slides = pg.locator(".slide")
    for i in range(slides.count()):
        png = os.path.join(out, f"_tmp{i}.png")
        slides.nth(i).screenshot(path=png)
        Image.open(png).convert("RGB").save(os.path.join(out, f"{prefix}-{i+1}.jpg"), quality=90)
        os.remove(png)
        print(os.path.join(out, f"{prefix}-{i+1}.jpg"))
    b.close()
