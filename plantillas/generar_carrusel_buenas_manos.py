"""Carrusel 'Tu paquete en buenas manos' (9-nov-2026), estilo principal blanco.
Uso: python3 -I plantillas/generar_carrusel_buenas_manos.py && python3 -I plantillas/render.py publicaciones/2026-11-09-carrusel-buenas-manos/diseno.html lancarg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo_blanco import page, feed

ICON = {
 "escudo": '<path d="M50 8 84 20v26c0 22-14 38-34 46C30 84 16 68 16 46V20Z" fill="none" stroke="#fff" stroke-width="8" stroke-linejoin="round"/><path d="M35 50l10 10 20-22" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
 "reloj": '<circle cx="50" cy="50" r="36" fill="none" stroke="#fff" stroke-width="8"/><path d="M50 30V50L63 59" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
 "pin": '<path d="M50 10C35 10 23 22 23 37 23 57 50 90 50 90S77 57 77 37C77 22 65 10 50 10Z" fill="none" stroke="#fff" stroke-width="8"/><circle cx="50" cy="37" r="10" fill="#fff"/>',
}
def ic(name, size=150):
    return (f'<div style="width:{size}px;height:{size}px;border-radius:50%;background:#E70A0F;display:grid;place-items:center;box-shadow:0 10px 24px rgba(231,10,15,.3)">'
            f'<svg viewBox="0 0 100 100" style="width:{int(size*.56)}px;height:{int(size*.56)}px">{ICON[name]}</svg></div>')

def paso(n, icon, titulo, sub, foto, pos="50% 50%", ph=None, top=600):
    return feed(photo=foto, photo_top=top, photo_h=ph, photo_pos=pos, fade=(8, 24), title=titulo, title_size=82, sub=sub,
                top={"logo": 70, "kick": 0, "h1": 330},
                extra=f'<div style="position:absolute;left:50%;top:205px;transform:translateX(-50%);z-index:4">{ic(icon, 110)}</div>'
                      f'<div style="position:absolute;left:70px;top:230px;font-family:Inter Display,Inter;font-weight:300;font-size:90px;color:transparent;-webkit-text-stroke:3px #E70A0F;z-index:4">0{n}</div>')

beneficios = "".join(
    f'<div style="display:flex;flex-direction:column;align-items:center;gap:22px;width:280px">{ic(i)}'
    f'<div style="font-size:36px;font-weight:800;color:#02462D;text-align:center;line-height:1.15">{t}</div></div>'
    for i, t in [("escudo", "Cuidado de<br>punta a punta"), ("reloj", "Puntualidad<br>de verdad"), ("pin", "Rutas que<br>conocemos")])

slides = [
    feed(photo="operario-de-montacargas-en-deposito-industrial.jpg", photo_top=560, photo_pos="50% 18%", fade=(8, 24),
         kick="Lancarg", title='Tu paquete<br><span class="r">en buenas manos</span>', title_size=96,
         sub='Deslizá y conocé <b>por qué →</b>', cta=False),
    paso(1, "escudo", 'Cuidado de<br><span class="r">punta a punta</span>', 'Del inicio <b>al destino</b>',
         "interior-de-deposito-san-juan-con-autoelevador-toyota.jpg", "50% 55%"),
    paso(2, "reloj", 'Puntualidad<br><span class="r">de verdad</span>', 'Camiones <b>todos los días</b>',
         "scania-blanca-cruzando-el-desierto-al-atardecer.jpg", "62% 50%", ph=640, top=560),
    paso(3, "pin", 'Rutas que conocemos<br><span class="r">de memoria</span>', 'Buenos Aires, Córdoba y Rosario<br><b>↔ San Juan y Mendoza</b>',
         "planchada-descarga-deposito-sj.jpg", "50% 60%"),
    feed(title='¿Querés<br><span class="r">tranquilidad?</span>', title_size=100, top={"logo": 70, "kick": 0, "h1": 260},
         extra=f'<div style="position:absolute;left:0;right:0;top:600px;display:flex;justify-content:center;gap:40px;z-index:4">{beneficios}</div>'
               '<div style="position:absolute;left:0;right:0;top:900px;text-align:center;z-index:4"><div style="font-size:54px;font-weight:800;color:#02462D">Trae con</div>'
               '<img src="../../marca/versiones/1-principal-color.png" style="width:520px;margin-top:10px"></div>'),
]
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "publicaciones", "2026-11-09-carrusel-buenas-manos")
open(os.path.join(d, "diseno.html"), "w").write(page(slides))
