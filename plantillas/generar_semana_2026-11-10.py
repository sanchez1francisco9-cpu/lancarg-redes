"""Semana 10 al 16 de noviembre de 2026 (historias nuevas, post y carrusel; estilo principal blanco).
Uso: python3 -I plantillas/generar_semana_2026-11-10.py  y después render.py en cada carpeta."""
import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo_blanco import page, story, feed
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
R = os.path.join(B, "publicaciones")
T = {"logo": 230, "kick": 0, "h1": 480}


def vert(foto, title, size=92, fade=(36, 48), sub=None, pos="50% 50%", top=0):
    """Foto vertical 9:16 de fondo completo."""
    return story(photo=foto, photo_top=top, photo_pos=pos, fade=fade, title=title, title_size=size, sub=sub, top=T)


def completa(foto, title, size=92, sub=None, fade=(0, 16), tope=None):
    """Foto horizontal (o vertical no 9:16) completa al ancho, apoyada abajo: no se recorta nada."""
    w, h = Image.open(os.path.join(B, "fotos", foto)).size
    ph = round(1080 * h / w)
    top = tope if tope is not None else 1920 - ph
    return story(photo=foto, photo_top=top, photo_h=ph, fade=fade, title=title, title_size=size, sub=sub, top=T)


historias = {
 "2026-11-10-historias": [
  vert("vertical/camion-scania-lancarg-en-muelle-logistico.jpg", 'Del inicio<br><span class="r">al destino</span>', size=110, fade=(30, 42),
       sub='Camiones <b>todos los días</b>'),
 ],
 "2026-11-11-historias": [
  completa("deposito-interior-completo.jpg", 'Menos demoras,<br><span class="r">más tranquilidad</span>', size=88, tope=780),
  completa("interior-deposito-bsas-con-mucha-mercaderia-variada.jpg", 'Un socio que<br><span class="r">mueve tu negocio</span>', size=92,
           sub='Reponé stock <b>sin viajar</b>'),
 ],
 "2026-11-12-historias": [
  completa("muestrario-de-cajas-con-el-logo-transportes-lancarg.jpg", 'Más que transporte:<br><span class="r">entregamos confianza</span>', size=78),
 ],
 "2026-11-13-historias": [
  vert("vertical/camion-en-deposito-bsas.jpg", 'Cobertura regional<br><span class="r">con trato cercano</span>', size=84, fade=(34, 46),
       sub='Buenos Aires · Córdoba · Rosario<br><b>↔ San Juan y Mendoza</b>'),
  vert("vertical/deposito-buenos-aires-ordenado.jpg", 'El plazo<br><span class="r">no es un detalle</span>', size=100, fade=(34, 46)),
 ],
 "2026-11-14-historias": [
  completa("almacen-deposito-ordenado-san-juan.jpg", 'Cuando el tiempo aprieta,<br><span class="r">la estructura hace<br>la diferencia</span>', size=72, tope=860),
 ],
 "2026-11-15-historias": [
  vert("vertical/3-camiones-lancarg-bajo-cielo-azul.jpg", 'Llegás más lejos<br><span class="r">con una logística<br>que te acompaña</span>', size=80, fade=(39, 50)),
  vert("vertical/camion-visto-de-atras-a-adelante.jpg", 'Conectando<br><span class="r">lo que importa</span>', size=104, fade=(32, 44)),
 ],
 "2026-11-16-historias": [
  vert("interior-deposito-sj-con-mercaderia-y-operario-manejando-forklif-camion-afuera.jpg",
       'Empresa sanjuanina,<br><span class="r">desde 1957</span>', size=90, fade=(40, 52)),
  completa("caja-de-carton-con-logo-de-transporte-lancarg.jpg", 'Cumplir<br><span class="r">lo acordado</span>', size=118,
           sub='Tu paquete, <b>en tiempo y forma</b>'),
 ],
}
for carpeta, slides in historias.items():
    d = os.path.join(R, carpeta); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "diseno.html"), "w").write(page(slides))

# ---- Post de una imagen (viernes 13): "Crecemos para llegar más lejos" (frase de Fran, 5-nov) ----
post = feed(photo="carga-de-auto-a-camion-usando-autoelevador.jpg", photo_top=48, photo_h=1302, photo_pos="50% 0%", fade=(30, 44),
            title='Crecemos para<br><span class="r">llegar más lejos</span>', title_size=92, top={"logo": 70, "kick": 0, "h1": 250})
d = os.path.join(R, "2026-11-13-post-crecemos"); os.makedirs(d, exist_ok=True)
open(os.path.join(d, "diseno.html"), "w").write(page([post]))

# ---- Carrusel (lunes 16): "¿Paquete suelto o pallet?" ----
CUT = "../../fotos/recortes/"
def placa(n, titulo, sub, foto, top=560, ph=None, pos="50% 50%", fade=(8, 24)):
    return feed(photo=foto, photo_top=top, photo_h=ph, photo_pos=pos, fade=fade, title=titulo, title_size=86, sub=sub,
                top={"logo": 70, "kick": 0, "h1": 300},
                extra=f'<div style="position:absolute;left:70px;top:205px;font-family:Inter Display,Inter;font-weight:300;font-size:90px;'
                      f'color:transparent;-webkit-text-stroke:3px #E70A0F;z-index:4">0{n}</div>')

carrusel = [
    feed(kick="Guía rápida", title='¿Paquete suelto<br><span class="r">o pallet?</span>', title_size=104,
         sub='Deslizá y mirá <b>cuál te conviene →</b>', cta=False,
         extra=f'<img src="{CUT}caja-png-con-fondo-transparente-con-logo-lancarg.png" style="position:absolute;left:40px;top:720px;width:470px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.25))">'
               f'<img src="{CUT}pallet-con-paquetes-lancarg-fondo-transparente.png" style="position:absolute;right:40px;top:640px;width:520px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.25))">'),
    placa(1, 'Paquete<br><span class="r">suelto</span>', 'Encomiendas y envíos chicos.<br><b>Un solo paquete también viaja</b>',
          "vertical/caja-de-envio-lancarg-en-estudio-verde.jpg", top=560, ph=790, pos="50% 62%"),
    placa(2, '<span class="r">Pallet</span>', 'Para comercios que reponen<br><b>mucha mercadería de una vez</b>',
          "deposito-industrial-amplio-y-ordenado.jpg", top=520, pos="50% 70%"),
    placa(3, 'Los dos viajan<br><span class="r">con el mismo cuidado</span>', 'Lo dejás en nuestras sucursales<br><b>o lo retiramos</b>',
          "camion-con-semi-de-frete-derecho.jpg", top=630, ph=720, pos="50% 60%", fade=(6, 22)),
    feed(title='¿No sabés<br><span class="r">cuál elegir?</span>', title_size=104, top={"logo": 70, "kick": 0, "h1": 300},
         sub='Te asesoramos <b>sin compromiso</b>', cta=False,
         extra='<div style="position:absolute;left:0;right:0;top:700px;text-align:center;z-index:4">'
               '<div style="font-size:46px;font-weight:700;color:#1d2b25">Cotizá tu envío por WhatsApp</div>'
               '<div style="display:inline-flex;align-items:center;gap:18px;margin-top:26px;background:#02462D;color:#fff;font-weight:900;font-size:76px;'
               'padding:20px 56px;border-radius:999px;box-shadow:0 14px 34px rgba(0,0,0,.2)">'
               '<svg width="64" height="64" viewBox="0 0 24 24" fill="#25D366"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg>'
               '264 454-3612</div>'
               '<div style="font-size:34px;font-weight:700;color:#4a524e;margin-top:30px">Camiones todos los días · Entrega en destino</div></div>'),
]
d = os.path.join(R, "2026-11-16-carrusel-suelto-o-pallet"); os.makedirs(d, exist_ok=True)
open(os.path.join(d, "diseno.html"), "w").write(page(carrusel))
