"""Semana 27-oct a 2-nov 2026 con el estilo principal (blanco + foto + logo a color).
Uso: python3 -I plantillas/generar_semana_2026-10-27.py  (escribe los diseno.html; después render.py)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo_blanco import page, story, feed

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "publicaciones")


def write(folder, slides):
    d = os.path.join(ROOT, folder); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "diseno.html"), "w").write(page(slides))


def hstory(photo, w, h, bottom=1760, fade=(0, 22), **k):
    """Historia con foto horizontal completa (sin recortar): ancho 1080, alto proporcional."""
    ph = round(1080 * h / w)
    return story(photo=photo, photo_top=bottom - ph, photo_h=ph, fade=fade, **k)


# ---------- Historias nuevas ----------
# Fotos 3:4 completas abajo (1080x1440, top 480): el texto va arriba, más compacto.
T = {"logo": 110, "kick": 290, "h1": 300}
TK = {"logo": 110, "kick": 290, "h1": 370}
F34 = dict(photo_top=480, photo_h=1440, fade=(12, 24))

write("2026-10-28-historia-nuestra-ruta", [
    hstory("camion-con-semi-de-frete-derecho.jpg", 1536, 1024, bottom=1730, fade=(0, 20),
           title='Tu paquete.<br>Nuestra ruta.<br><span class="r">Un mismo objetivo.</span>', title_size=96),
])

write("2026-10-29-historia-depositos-propios", [
    story(photo="deposito-interior-completo.jpg", **F34, top=TK,
          kick="Depósitos propios", title='Una base sólida<br><span class="r">para tus envíos</span>', title_size=92,
          sub='San Juan <b>·</b> Buenos Aires'),
])

write("2026-10-30-historias", [
    story(photo="vertical/deposito-buenos-aires-ordenado.jpg", photo_top=480, photo_h=1440, photo_pos="50% 70%", fade=(12, 24),
          top=T, title='¿Qué podés<br><span class="r">enviar?</span>', title_size=104,
          sub='Paquetes <b>·</b> Bultos <b>·</b> Mercadería <b>·</b> Pallets'),
    story(photo="camion-lateral-conductor.jpg", **F34, top=T,
          title='La confianza<br><span class="r">también se transporta</span>', title_size=84),
])

write("2026-10-31-historia-preparados", [
    hstory("camion-de-frente-izquierdo.jpg", 1402, 1122, bottom=1740, fade=(0, 22),
           title='Preparados<br><span class="r">para el camino</span>', title_size=104,
           sub='Flota propia y moderna'),
])

write("2026-11-01-historias", [
    hstory("scania-blanca-cruzando-el-desierto-al-atardecer.jpg", 1600, 813, bottom=1720, fade=(0, 26),
           kick="Desde 1957", title='Experiencia y<br>compromiso<br><span class="r">en cada recorrido</span>', title_size=80,
           top={"logo": 330, "kick": 680, "h1": 770}),
    hstory("camion-en-deposito-bsas.jpg", 1450, 1085, bottom=1740, fade=(0, 18),
           title='Conectamos<br>destinos.<br><span class="r">Movemos<br>oportunidades.</span>', title_size=84,
           sub='Buenos Aires, Córdoba y Rosario<br><b>↔</b> San Juan y Mendoza', top={"logo": 200, "kick": 0, "h1": 420}),
])

write("2026-11-02-historias", [
    story(photo="planchada-con-mercaderia.jpg", **F34, top={"logo": 90, "kick": 270, "h1": 345},
          kick="Cotizá en 3 pasos", title='Escribinos.<br>Te asesoramos.<br><span class="r">Coordinamos el retiro.</span>',
          title_size=70),
    hstory("camion-visto-de-atras-a-adelante.jpg", 1448, 1086, bottom=1740, fade=(0, 18),
           title='Cuidar la flota<br><span class="r">es cuidar tu envío</span>', title_size=100,
           sub='Flota propia y moderna'),
])

# ---------- Feed lunes 2-nov: carrusel "Lo que te cuesta un paquete que no llega" ----------
def num(n):
    return (f'<div style="position:absolute;left:60px;top:250px;width:110px;height:110px;border-radius:50%;background:#E70A0F;'
            f'color:#fff;font:900 64px Inter;display:flex;align-items:center;justify-content:center;z-index:4">{n}</div>')

write("2026-11-02-carrusel-paquete-que-no-llega", [
    feed(photo="almacen-deposito-ordenado-san-juan.jpg", photo_top=530, photo_h=820, photo_pos="50% 90%", fade=(0, 16),
         kick="Paquetería", title='Un paquete que no llega<br><span class="r">te cuesta mucho más</span>', title_size=72,
         sub='que el envío <b>→</b>', cta=False),
    feed(photo="interior-deposito-bsas-con-mucha-mercaderia-variada.jpg", photo_top=520, photo_h=830, fade=(0, 18),
         title='Frena tu venta<br><span class="r">o tu reposición</span>', title_size=84, extra=num(1), cta=False),
    feed(photo="deposito-industrial-amplio-y-ordenado.jpg", photo_top=520, photo_h=830, photo_pos="50% 90%", fade=(0, 16),
         title='Suma <span class="r">costos</span>', title_size=96, sub='Reclamos, reenvíos <b>y tiempo perdido</b>',
         extra=num(2), cta=False),
    feed(photo="exterior-deposito-con-mercaderia-y-camion.jpg", photo_top=520, photo_h=830, fade=(0, 18),
         title='Tu cliente<br><span class="r">pierde confianza</span>', title_size=84, extra=num(3), cta=False),
    feed(photo="autoelevador-descargando-camion-con-empleados.jpg", photo_top=520, photo_h=830, fade=(0, 18),
         title='¿Querés tranquilidad?<br><span class="r">Trae con</span>', title_size=80,
         top={"logo": 300, "kick": 0, "h1": 90},
         extra='<div class="sub" style="top:470px;font-size:30px">Camiones todos los días <b>·</b> Entregamos en destino</div>'),
])
