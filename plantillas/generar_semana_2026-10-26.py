"""Semana 26-oct a 1-nov 2026 con el estilo principal (blanco + foto + logo a color).
Uso: python3 -I plantillas/generar_semana_2026-10-26.py  (escribe los diseno.html; después render.py)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo_blanco import page, story, feed

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "publicaciones")


def write(folder, slides):
    d = os.path.join(ROOT, folder); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "diseno.html"), "w").write(page(slides))


SUC = [("San Juan", "Ruta 40 545 Norte, Chimbas", "264 454-3612"),
       ("Mendoza", "Mitre 2671, Guaymallén", "261 240-6204"),
       ("Buenos Aires", "Pergamino 3751, C.T.C. Villa Soldati", "11 3779-5919"),
       ("Córdoba", "La Cordillera 3774", "351 311-2698"),
       ("Rosario", "Río de Janeiro 2510", "341 364-0498")]
WA = '<svg width="34" height="34" viewBox="0 0 24 24" fill="#25D366" style="flex:none"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg>'
cards = "".join(
    f'<div style="display:flex;justify-content:space-between;align-items:center;border:3px solid #e3e8e5;border-left:10px solid #E70A0F;border-radius:18px;padding:22px 30px;margin-top:18px;background:#fff">'
    f'<div><div style="font-size:40px;font-weight:900;color:#02462D">{n}</div><div style="font-size:28px;font-weight:500;color:#4a524e;margin-top:4px">{a}</div></div>'
    f'<div style="display:flex;align-items:center;gap:10px;font-size:36px;font-weight:800;color:#02462D;white-space:nowrap">{WA}{t}</div></div>'
    for n, a, t in SUC)

write("2026-10-26-carrusel-sucursales", [
    feed(photo="frente-deposito-bsas-en-el-ctc-de-villa-soldati.jpg", photo_top=470, photo_pos="50% 40%", fade=(10, 30),
         kick="Estamos cerca", title='5 sucursales para<br><span class="r">tus envíos</span>', title_size=88,
         sub='Deslizá y encontrá <b>la tuya →</b>', cta=False),
    feed(title='Nuestras <span class="r">sucursales</span>', title_size=72, top={"logo": 60, "kick": 0, "h1": 200}, cta=False,
         extra=f'<div style="position:absolute;left:70px;right:70px;top:290px">{cards}</div>'),
])

write("2026-10-26-historias", [
    story(photo="frente-deposito-bsas-en-el-ctc-de-villa-soldati.jpg", photo_top=760, photo_pos="50% 40%", fade=(8, 22),
          kick="Estamos cerca", title='5 <span class="r">sucursales</span>', sub='San Juan · Mendoza · Buenos Aires<br>Córdoba · Rosario'),
    story(cut="cajas-de-transporte-apiladas-con-logo-fondo-transparente.png", cut_top=1020, cut_w=82,
          title='Empezá la semana<br>con tu envío<br><span class="r">resuelto</span>', title_size=96),
])

write("2026-10-27-historias", [
    story(photo="vertical/scania-cruzando-el-desierto.jpg", photo_top=0, fade=(40, 56),
          title='Llevamos lo que necesitás,<br><span class="r">hasta donde<br>lo necesitás</span>', title_size=78,
          top={"logo": 230, "kick": 0, "h1": 470}),
    story(photo="vertical/autoelevador-descargando-camion-con-empleados.jpg", photo_top=300, fade=(24, 36),
          title='Cuidamos tu paquete<br><span class="r">como propio</span>', title_size=86,
          sub='Desde que lo recibimos <b>hasta que llega</b>'),
])
