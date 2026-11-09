"""Reels de la semana 10-16 nov 2026 (estilo principal blanco), basados en publicaciones/2026-11-08-reel-un-solo-paquete.
Uso: python3 -I plantillas/generar_reels_2026-11-10.py y despues render_video.py en cada carpeta."""
import os, re
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
base = open(os.path.join(B, "publicaciones/2026-11-08-reel-un-solo-paquete/diseno.html")).read()
head = base[:base.index('<div id="stage">')]
DIAG = '<div class="d tr1"></div><div class="d tr2"></div><div class="d br1"></div><div class="d br2"></div><div class="d br3"></div>'
LOGO = '<img class="lg" src="../../marca/versiones/1-principal-color.png">'
D = 3.3

def gancho(i, titulo, cut, size=96, cut_top=930, cut_w=760, foto=None):
    img = (f'<img class="ph" src="../../fotos/{foto}">' if foto else "")
    pk = (f'<div data-in="0.5"><img class="pk" src="../../fotos/recortes/{cut}" style="top:{cut_top}px;width:{cut_w}px;margin-left:-{cut_w//2}px"></div>' if cut else "")
    return (f'<div class="scene w" id="s{i}" data-start="{i*D:.1f}" data-end="{(i+1)*D:.1f}" data-nologo>{img}{DIAG}{LOGO}'
            f'<div class="c" style="top:450px"><h2 data-in="0.2" style="font-size:{size}px">{titulo}</h2><div class="bar" data-in="0.6"></div></div>{pk}</div>')

def paso(i, n, titulo, foto):
    return (f'<div class="scene w" id="s{i}" data-start="{i*D:.1f}" data-end="{(i+1)*D:.1f}" data-nologo><img class="ph" src="../../fotos/{foto}">{DIAG}{LOGO}'
            f'<div class="c" style="top:370px"><div class="num" data-in="0.15">0{n}</div><h2 data-in="0.3">{titulo}</h2></div></div>')

def cierre(i):
    a = i * D; b = a + 5.35
    return (f'<div class="scene end white" id="fin" data-start="{a:.1f}" data-end="{b:.2f}" data-nologo>'
            '<div class="endq" style="top:380px" data-in="0.15"><h2 style="margin:0">¿Querés <em>tranquilidad</em>?</h2></div>'
            '<div class="endq" style="top:520px" data-in="0.55"><div class="trae">Transportá tu mercadería con</div></div>'
            '<div class="endq" style="top:1110px" data-in="2.0"><div class="pill" style="margin:0"><span style="font-size:60px">📲</span><span>Cotizá por WhatsApp<small>264 454-3612</small></span></div></div>'
            f'</div></div>\n<script>window.OVERLAY = [{{src: "../../marca/logo-lancarg-animado-horizontal.mp4", start: {a+0.35:.2f}, x: 0, y: 715, w: 1080, crop: "1920:520:0:270"}}];</script>\n'
            '<script src="../../plantillas/motion.js"></script>\n</body></html>')

reels = {
 "2026-11-11-reel-tres-errores": [
  gancho(0, '3 errores<br>que <em>complican</em><br>tu envío', "cajas-de-transporte-apiladas-con-logo-fondo-transparente.png", size=104, cut_top=960, cut_w=820),
  paso(1, 1, 'Embalar mal<br><em>tu paquete</em>', "muchas-cajas-en-el-deposito.jpg"),
  paso(2, 2, 'No declarar<br><em>el valor</em>', "deposito-bsas-con-paquetes.jpg"),
  paso(3, 3, 'Dejarlo para<br><em>último momento</em>', "planchada-deposito-san-juan.jpg"),
  gancho(4, 'Te asesoramos<br><em>antes de enviar</em>', "caja-png-con-fondo-transparente-con-logo-lancarg.png", size=100, cut_top=900),
 ],
 "2026-11-15-reel-seguridad": [
  gancho(0, 'La seguridad<br>empieza <em>antes<br>de cada viaje</em>', None, size=96, foto="vertical/camion-frente-izquierdo.jpg"),
  paso(1, 1, 'Controlamos<br><em>la flota</em>', "camion-lateral-conductor.jpg"),
  paso(2, 2, 'Revisamos<br><em>cada carga</em>', "planchada-con-mercaderia.jpg"),
  paso(3, 3, 'Cuidamos<br><em>cada paquete</em>', "deposito-bsas-con-cajas.jpg"),
  gancho(4, 'Seguridad en<br><em>cada kilómetro</em>', "pallet-con-paquetes-lancarg-fondo-transparente.png", size=104, cut_top=860, cut_w=700),
 ],
}
for carpeta, esc in reels.items():
    d = os.path.join(B, "publicaciones", carpeta); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "diseno.html"), "w").write(head + '<div id="stage">\n' + "\n".join(esc) + "\n" + cierre(len(esc)))
