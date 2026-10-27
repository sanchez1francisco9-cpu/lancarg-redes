import sys
sys.path.insert(0,'plantillas')
from estilo_blanco import page, feed, story
F='../../fotos/'
def img(src,style): return f'<img src="{F}{src}" style="position:absolute;{style}">'
slides=[
 feed(kick="Empresa familiar", title='El transporte lo hacen<br><span class="r">las personas</span>', title_size=68,
      sub='No son solo <b>camiones</b>',
      extra=img("hombre-entregando-caja-con-logo-de-lancarg-a-mujer.jpg","left:0;top:610px;width:1080px;-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 14%);mask-image:linear-gradient(180deg,transparent 0%,#000 14%)")),
 feed(kick="Depósitos propios", title='El mundo evoluciona,<br><span class="r">nosotros también</span>', title_size=82,
      sub='San Juan · Buenos Aires',
      extra=img("interior-deposito-sj-con-mercaderia-y-operario-manejando-forklif-camion-afuera.jpg","left:0;top:610px;width:1080px;height:740px;object-fit:cover;object-position:50% 62%;-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 16%);mask-image:linear-gradient(180deg,transparent 0%,#000 16%)")),
 story(title='En cada kilómetro,<br><span class="r">tu envío es<br>nuestra prioridad</span>', title_size=92, top={"logo":200,"kick":0,"h1":420},
      extra=img("frente-imponente-del-scania-r450.jpg","left:90px;top:760px;width:900px;-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 10%),linear-gradient(90deg,transparent 0%,#000 8%,#000 92%,transparent 100%);-webkit-mask-composite:source-in;mask-image:linear-gradient(180deg,transparent 0%,#000 10%),linear-gradient(90deg,transparent 0%,#000 8%,#000 92%,transparent 100%);mask-composite:intersect")),
]
open('publicaciones/pruebas-nuevas/diseno.html','w').write(page(slides))
# variante dividida: texto a la izquierda, foto a la derecha (historia)
split='''<div class="slide story">
<img src="../../fotos/camiondecostadocerca.jpg" style="position:absolute;right:0;top:560px;height:1360px;-webkit-mask-image:linear-gradient(90deg,transparent 0%,#000 5%),linear-gradient(180deg,transparent 0%,#000 12%);-webkit-mask-composite:source-in;mask-image:linear-gradient(90deg,transparent 0%,#000 5%),linear-gradient(180deg,transparent 0%,#000 12%);mask-composite:intersect">
<div class="d tr1" style="height:190px"></div><div class="d tr2" style="height:190px"></div>
<img class="logo" src="../../marca/versiones/1-principal-color.png" style="left:70px;transform:none;top:150px;width:470px">
<div style="position:absolute;left:70px;top:430px;width:470px;z-index:4">
 <div style="font-size:44px;font-weight:800;letter-spacing:.14em;color:#1d2b25">DESDE</div>
 <div style="font-family:'Inter Display',Inter;font-weight:900;font-size:200px;line-height:.85;letter-spacing:-.04em;color:#E70A0F">1957</div>
 <div style="width:120px;height:6px;background:#E70A0F;margin:40px 0 34px"></div>
 <div style="font-family:'Inter Display',Inter;font-weight:900;font-size:64px;line-height:1.02;letter-spacing:-.02em;text-transform:uppercase;color:#02462D;text-shadow:0 0 30px #fff">Trayectoria<br>que inspira<br><span style="color:#E70A0F">confianza</span></div>
</div>
<div class="d br1"></div><div class="d br2"></div><div class="d br3"></div>
<div class="cta"><small>Cotizá por WhatsApp</small>264 454-3612</div>
</div>'''
s=open('publicaciones/pruebas-nuevas/diseno.html').read().replace('</body>',split+'\n</body>')
open('publicaciones/pruebas-nuevas/diseno.html','w').write(s)
