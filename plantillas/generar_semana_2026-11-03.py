"""Semana 3 al 9 de noviembre de 2026 (historias nuevas, estilo principal).
Uso: python3 -I plantillas/generar_semana_2026-11-03.py  y despues render.py en cada carpeta."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo_blanco import page, story
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "publicaciones")
T = {"logo": 230, "kick": 0, "h1": 480}
def vert(foto, title, size=92, fade=(36, 48), sub=None, pos="50% 50%"):
    return story(photo=foto, photo_top=0, photo_pos=pos, fade=fade, title=title, title_size=size, sub=sub, top=T)
def apaisada(foto, title, size=92, top=660, sub=None, pos="50% 50%"):
    return story(photo=foto, photo_top=top, photo_pos=pos, fade=(4, 18), title=title, title_size=size, sub=sub, top=T)
dias = {
 "2026-11-04-historias": [
  story(cut="cajas-de-transporte-apiladas-con-logo-fondo-transparente.png", cut_top=720, cut_w=90, top=T, title_size=70,
        title='Tardaste más en leer esto<br><span class="r">que en mandar tu paquete</span>'),
  vert("vertical/interior-deposito-bsas-con-mucha-mercaderia.jpg", 'Tu mercadería de<br>Flores y Once,<br><span class="r">en tu local</span>', fade=(38, 50)),
 ],
 "2026-11-05-historias": [
  story(photo="hombre-entregando-caja-con-logo-de-lancarg-a-mujer.jpg", photo_top=1200, photo_h=720, fade=(0, 12), title_size=104, top={"logo": 230, "kick": 0, "h1": 480},
        title='El transporte<br>lo hacen<br><span class="r">las personas</span>', sub='No son solo <b>camiones</b>'),
 ],
 "2026-11-06-historias": [
  vert("vertical/interior-deposito-bsas-con-cajas-a-la-izquierda-y-pallets-a-la-derecha.jpg", 'Logística que<br><span class="r">impulsa tus ventas</span>', fade=(34, 46)),
  story(photo="camion-scania-lancarg-bajo-cielo-azul.jpg", photo_top=300, photo_h=1920, fade=(18, 30), title='Eficiencia en<br><span class="r">cada kilómetro</span>', title_size=92, top=T),
 ],
 "2026-11-08-historias": [
  story(photo="camion-scania-al-atardecer-entre-montanas.jpg", photo_top=150, photo_h=1920, fade=(27, 34), title='Experiencia que<br><span class="r">acompaña cada destino</span>', title_size=74, top=T),
  apaisada("deposito-bsas.jpg", 'Cada traslado exige<br><span class="r">cuidado y compromiso</span>', size=76, top=700, pos="50% 0%"),
 ],
 "2026-11-09-historias": [
  story(photo="exterior-deposito-con-mercaderia-y-camion.jpg", photo_top=1110, photo_h=810, fade=(0, 14), title_size=112, top=T,
        title='La confianza<br>empieza en<br><span class="r">el compromiso</span>'),
  apaisada("camion-con-carga-paletizada-y-lona-verde.jpg", 'Traslado seguro<br><span class="r">y responsable</span>'),
 ],
}
for carpeta, slides in dias.items():
    d = os.path.join(R, carpeta); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "diseno.html"), "w").write(page(slides))
