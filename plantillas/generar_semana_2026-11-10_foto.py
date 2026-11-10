"""Semana 10-16 nov 2026, segunda tanda: Fran (10-nov) pidió menos blanco y más piezas con el estilo "foto completa".
Rehace las historias que quedaban en el estilo blanco, suma el post del miércoles 11 y pasa el carrusel del lunes 16.
Uso: python3 -I plantillas/generar_semana_2026-11-10_foto.py  y después render.py en cada carpeta."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import estilo_foto as EF
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "publicaciones")
V = "vertical/"
IN = 0.62  # sombra más fuerte arriba para fotos de interior (techo de depósito en vez de cielo)

piezas = {
 # ---- historias ----
 "2026-11-11-historias-foto": [
  EF.foto("story", V + "autoelevador-descargando-camion-con-empleados.jpg", "Menos demoras", "más tranquilidad", "Camiones todos los días", top=230),
  EF.foto("story", V + "interior-deposito-bsas-con-mucha-mercaderia.jpg", "Un socio que<br>mueve tu<br>negocio", box="Reponé stock sin viajar",
          top=200, h1_size=124, shade=IN),
 ],
 "2026-11-12-historia-foto": [
  EF.foto("story", V + "caja-de-envio-lancarg-en-estudio-verde.jpg", "Más que<br>transporte", "entregamos confianza", top=210, shade=0.25),
 ],
 "2026-11-13-historia-foto-2": [
  EF.foto("story", V + "deposito-buenos-aires-ordenado.jpg", "El plazo", "no es un detalle", "Cumplimos lo acordado", top=220, shade=IN),
 ],
 "2026-11-14-historia-foto": [
  EF.foto("story", V + "interior-deposito-bsas-con-cajas-a-la-izquierda-y-pallets-a-la-derecha.jpg", "Cuando el<br>tiempo aprieta",
          "la estructura hace la diferencia", "Depósitos propios", top=200, h1_size=120, h2_size=52, shade=IN),
 ],
 "2026-11-15-historia-foto-2": [
  EF.foto("story", V + "camion-visto-de-atras-a-adelante.jpg", "Conectando", "lo que importa", "Buenos Aires · Córdoba · Rosario<br>↔ San Juan y Mendoza",
          top=230, box_size=40, shade=0.5),
 ],
 "2026-11-16-historias-foto": [
  EF.foto("story", V + "scania-cruzando-el-desierto.jpg", "Empresa<br>sanjuanina", "desde 1957", top=230),
  EF.foto("story", V + "camion-frente-izquierdo.jpg", "Cumplir<br>lo acordado", "tu paquete, en tiempo y forma", top=200, shade=0.5),
 ],
 # ---- post del miércoles 11 (reemplaza el reel que Fran sacó) ----
 "2026-11-11-post-traslado-seguro": [
  EF.foto("feed", V + "camion-scania-lancarg-bajo-un-cielo-azul.jpg", "Traslado<br>seguro", "y responsable", "Cuidamos cada paquete", top=120, pos="50% 10%"),
 ],
}

# ---- carrusel del lunes 16: "¿Paquete suelto o pallet?" ----
def num(n):
    return (f'<div style="position:absolute;left:0;right:0;top:70px;text-align:center;font-family:Inter Display,Inter;font-weight:300;font-size:96px;'
            f'color:transparent;-webkit-text-stroke:3px #fff;text-shadow:none">0{n}</div>')

piezas["2026-11-16-carrusel-suelto-o-pallet-foto"] = [
    EF.foto("feed", V + "interior-deposito-bsas-con-mucha-mercaderia.jpg", "¿Paquete suelto<br>o pallet?", box="Deslizá y mirá cuál te conviene →",
            top=150, h1_size=104, box_size=42, shade=IN, cta=False, pos="50% 30%"),
    EF.foto("feed", V + "caja-de-envio-lancarg-en-estudio-verde.jpg", "Paquete<br>suelto", "Encomiendas y envíos chicos",
            "Un solo paquete también viaja", top=200, h1_size=112, box_size=42, shade=0.25, pos="50% 20%", extra=num(1)),
    EF.foto("feed", "deposito-industrial-amplio-y-ordenado.jpg", "Pallet", "Para comercios que reponen<br>mucha mercadería de una vez",
            top=200, h1_size=124, shade=IN, pos="50% 50%", extra=num(2)),
    EF.foto("feed", V + "3-camiones-lancarg-bajo-cielo-azul.jpg", "Los dos viajan", "con el mismo cuidado",
            "Lo dejás en nuestras sucursales o lo retiramos", top=200, h1_size=100, box_size=36, pos="50% 15%", extra=num(3)),
    EF.foto("feed", V + "camion-scania-lancarg-en-muelle-logistico.jpg", "¿No sabés<br>cuál elegir?", "Te asesoramos sin compromiso",
            "Cotizá por WhatsApp: 264 454-3612", top=120, h1_size=104, box_size=40, cta=False, pos="50% 10%"),
]

for carpeta, slides in piezas.items():
    d = os.path.join(R, carpeta); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "diseno.html"), "w").write(EF.page(slides))
    print(carpeta)
