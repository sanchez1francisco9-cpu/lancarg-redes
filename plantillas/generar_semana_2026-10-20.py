"""Genera los diseno.html de la semana 20 al 26 de octubre de 2026."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = "../../fotos/"
LOGO = "../../marca/logo-lancarg-sobre-verde.png"

CSS = """
:root{--g:#02462D;--g2:#013322;--r:#E70A0F;--w:#fff;--soft:#9fdcbb}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#777;font-family:Inter,sans-serif}
.slide{width:1080px;position:relative;overflow:hidden;color:var(--w);margin-bottom:20px;background:var(--g2)}
.feed{height:1350px}.story{height:1920px}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(1,40,26,.92) 0%,rgba(1,40,26,.6) 13%,rgba(1,40,26,0) 27%,rgba(1,40,26,0) 40%,rgba(1,51,34,.93) 68%,var(--g2) 100%)}
.shade.top{background:linear-gradient(180deg,rgba(1,51,34,.95) 0%,rgba(1,51,34,.85) 30%,rgba(1,51,34,0) 55%)}
.logo{position:absolute;top:60px;left:60px;width:400px;filter:drop-shadow(0 3px 10px rgba(0,0,0,.55));z-index:5}
.story .logo{top:120px;left:64px}
.logo.br{top:auto;left:auto;right:56px;bottom:56px;width:280px}
.txt{position:absolute;left:72px;right:72px;bottom:110px;z-index:4}
.story .txt{bottom:260px}
.txt.top{top:220px;bottom:auto}
.story .txt.top{top:330px}
.kicker{display:inline-block;background:var(--r);font-weight:800;font-size:30px;letter-spacing:.06em;text-transform:uppercase;padding:12px 22px;border-radius:6px;margin-bottom:30px}
h1{font-family:"Inter Display",Inter;font-weight:900;font-size:100px;line-height:.98;letter-spacing:-.02em}
.story h1{font-size:112px}
h1 em{font-style:normal;color:#7fd3a6}
h2{font-family:"Inter Display",Inter;font-weight:900;font-size:76px;line-height:1;letter-spacing:-.015em}
.sub{font-size:44px;font-weight:500;margin-top:30px;line-height:1.25;color:#e6f5ec}
.num{font-family:"Inter Display";font-weight:900;font-size:180px;line-height:.8;color:var(--r);margin-bottom:24px}
.pill{display:inline-flex;align-items:center;gap:18px;margin-top:40px;background:#fff;color:var(--g);font-weight:800;font-size:46px;padding:24px 42px;border-radius:999px}
.list{margin-top:44px;display:flex;flex-direction:column;gap:26px}
.li{display:flex;align-items:center;gap:24px;font-size:42px;font-weight:600}
.dot{flex:none;width:52px;height:52px;border-radius:50%;background:var(--r);display:grid;place-items:center;font-size:30px;font-weight:900}
.bar{position:absolute;left:0;right:0;bottom:0;height:86px;background:var(--g);display:flex;align-items:center;justify-content:center;gap:34px;font-size:26px;font-weight:700;letter-spacing:.03em;color:var(--soft);z-index:6}
.bar b{color:#fff;font-weight:700}
.step{position:absolute;top:64px;right:64px;z-index:5;background:var(--r);font-weight:900;font-size:34px;padding:10px 24px;border-radius:999px}
.card{background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.15);border-radius:28px;padding:30px 36px;margin-top:22px}
.card .t{font-size:40px;font-weight:800}
.card .d{font-size:32px;font-weight:500;color:#cfe9da;margin-top:8px}
.card .p{font-size:36px;font-weight:700;margin-top:10px;display:flex;align-items:center;gap:12px}
.mr{display:flex;gap:30px;align-items:flex-start}
.mito{font-size:44px;font-weight:800;color:#ffb3b5}
"""

WA = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="#25D366"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg>'
BAR = '<div class="bar"><span><b>Camión</b> todos los días</span><span>·</span><span><b>Carga</b> asegurada</span><span>·</span><span><b>Entrega</b> en destino</span></div>'
WAPILL = '<div class="pill">' + WA.format(s=48) + '264 454-3612</div>'


def photo(name, pos="50% 50%"):
    fit = ";object-fit:contain;object-position:50% 14%" if name.startswith(("caja-de-carton", "muestrario")) else ""
    return f'<img class="bg" src="{F}{name}.jpg" style="object-position:{pos}{fit}">'


def page(slides):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(slides)}</body></html>'


def story(img, body, pos="50% 50%", shade="", logo=True, top=False):
    return (f'<div class="slide story">{photo(img,pos)}<div class="shade {shade}"></div>'
            + (f'<img class="logo" src="{LOGO}">' if logo else '')
            + f'<div class="txt {"top" if top else ""}">{body}</div></div>')


def write(folder, slides):
    d = os.path.join(ROOT, "publicaciones", folder)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "diseno.html"), "w") as fh:
        fh.write(page(slides))
    print(folder)


# ---------- HISTORIAS (2 por día) ----------
H = {
 "2026-10-20-historias": [
   story("camion-scania-al-atardecer-entre-montanas", '<div class="kicker">Buenos Aires → San Juan</div><h1>Camión <em>todos</em> los días.</h1><div class="sub">Tu mercadería no espera.</div>', "50% 40%"),
   story("caja-de-carton-con-logo-de-transporte-lancarg", '<h1>¿Tenés que traer una caja?</h1><div class="sub">Cotizá en minutos por WhatsApp.</div>' + WAPILL, "50% 45%"),
 ],
 "2026-10-21-historias": [
   story("deposito-bsas-con-cajas", '<div class="kicker">Comercios</div><h1>¿Comprás en <em>Flores</em> u <em>Once</em>?</h1><div class="sub">Lo dejás en nuestras receptorías y te lo traemos a San Juan.</div>'),
   story("hombre-entregando-caja-con-logo-de-lancarg-a-mujer", '<h1>Retiramos y <em>entregamos</em>.</h1><div class="sub">Retiro a domicilio y última milla cubierta.</div>', "40% 50%"),
 ],
 "2026-10-22-historias": [
   story("muestrario-de-cajas-con-el-logo-transportes-lancarg", '<div class="mito">✕ Mito: "Solo llevan cargas grandes".</div><h1 style="margin-top:30px">Realidad: <em>una sola caja</em> también viaja.</h1>', "50% 50%"),
   story("camion-con-carga-paletizada-y-lona-verde", '<h1>Tu carga, <em>asegurada</em>.</h1><div class="sub">De punta a punta del viaje.</div>', "50% 50%"),
 ],
 "2026-10-23-historias": [
   story("tres-camiones-lancarg-en-el-patio-logistico", '<div class="kicker">Desde 1957</div><h1>Casi 70 años en la ruta.</h1><div class="sub">Una empresa familiar sanjuanina.</div>', "50% 50%"),
   story("planchada-deposito-san-juan", '<h2>Sucursal San Juan</h2><div class="card"><div class="t">Ruta 40 545 Norte, Chimbas</div><div class="d">Lunes a viernes de 8 a 16 h · Sábados de 8 a 12:30 h</div><div class="p">' + WA.format(s=40) + '264 454-3612</div></div>', "50% 50%"),
 ],
 "2026-10-24-historias": [
   story("muestrario-de-cajas-con-el-logo-transportes-lancarg", '<div class="kicker">Tip de envío</div><h2>Cómo embalar bien tu caja</h2><div class="list"><div class="li"><span class="dot">1</span>Caja firme, sin huecos adentro</div><div class="li"><span class="dot">2</span>Cinta en forma de H</div><div class="li"><span class="dot">3</span>Datos de destino bien visibles</div></div>', "50% 50%"),
   story("camiondecostadocerca", '<div class="kicker">Nuestro corredor</div><h1>Buenos Aires, Córdoba y Rosario → <em>San Juan y Mendoza</em>.</h1>', "50% 50%"),
 ],
 "2026-10-25-historias": [
   story("camion-scania-lancarg-bajo-cielo-azul", '<h1>Feliz domingo.</h1><div class="sub">Mañana arrancamos otra semana de envíos.</div>', "50% 40%"),
   story("interior-deposito-bsas-con-mucha-mercaderia-variada", '<div class="kicker">Comercios</div><h1>Reponé stock <em>sin viajar</em>.</h1><div class="sub">Comprás en Buenos Aires, lo recibís en tu local.</div>'),
 ],
 "2026-10-26-historias": [
   story("frente-deposito-bsas-en-el-ctc-de-villa-soldati", '<h2>5 sucursales</h2><div class="sub" style="font-size:52px;font-weight:800;color:#fff">San Juan · Mendoza · Buenos Aires · Córdoba · Rosario</div>', "50% 50%"),
   story("caja-de-carton-con-logo-de-transporte-lancarg", '<h1>Empezá la semana con tu envío resuelto.</h1>' + WAPILL, "50% 45%"),
 ],
}

# ---------- FEED ----------
def feed(img, body, pos="50% 50%", shade="", step=None, bar=True, logo=True, top=False):
    return (f'<div class="slide feed">{photo(img,pos)}<div class="shade {shade}"></div>'
            + (f'<img class="logo" src="{LOGO}">' if logo else '')
            + (f'<div class="step">{step}</div>' if step else '')
            + f'<div class="txt {"top" if top else ""}" style="bottom:{"150px" if bar else "110px"}">{body}</div>'
            + (BAR if bar else '') + '</div>')

FEED = {
 "2026-10-23-carrusel-viaje-de-tu-caja": [
   feed("caja-de-carton-con-logo-de-transporte-lancarg", '<div class="kicker">Paso a paso</div><h1>El viaje de <em>tu caja</em>.</h1><div class="sub">De Buenos Aires a tu puerta en San Juan. Deslizá →</div>', "50% 45%"),
   feed("deposito-bsas-con-cajas", '<div class="num">1</div><h2>Recepción</h2><div class="sub">La dejás en nuestras receptorías o te la retiramos.</div>', step="1/4"),
   feed("empleados-descargando-un-camion", '<div class="num">2</div><h2>Carga</h2><div class="sub">La clasificamos y la cargamos con cuidado.</div>', step="2/4"),
   feed("camion-scania-lancarg-en-el-playon-unerquicklich", '<div class="num">3</div><h2>Viaje</h2><div class="sub">Sale en camión propio. Hay camión todos los días.</div>', step="3/4"),
   feed("hombre-entregando-caja-con-logo-de-lancarg-a-mujer", '<div class="num">4</div><h2>Entrega</h2><div class="sub">Llega a destino y te la entregamos.</div>' + WAPILL, "40% 40%", step="4/4"),
 ],
 "2026-10-25-desde-1957": [
   feed("camion-scania-al-atardecer-entre-montanas", '<div class="kicker">Desde 1957</div><h1>Casi 70 años <em>en la ruta</em>.</h1><div class="sub">Gracias a cada cliente que nos confía su carga.</div>', "50% 40%"),
 ],
}

SUC = [
  ("San Juan", "Ruta 40 545 Norte, Chimbas", "264 454-3612"),
  ("Mendoza", "Mitre 2671, Guaymallén", "261 240-6204"),
  ("Buenos Aires", "Pergamino 3751, C.T.C. Villa Soldati", "11 3779-5919"),
  ("Córdoba", "La Cordillera 3774", None),
  ("Rosario", "Río de Janeiro 2510", "341 364-0498"),
]
cards = "".join(
  f'<div class="card" style="padding:28px 34px;margin-top:20px"><div class="mr"><div style="flex:1"><div class="t" style="font-size:44px">{n}</div><div class="d" style="font-size:32px">{a}</div></div>'
  + (f'<div class="p" style="font-size:38px;margin-top:6px">{WA.format(s=40)}{p}</div>' if p else '') + '</div></div>'
  for n, a, p in SUC)
FEED["2026-10-26-carrusel-sucursales"] = [
  feed("frente-deposito-bsas-en-el-ctc-de-villa-soldati", '<div class="kicker">Estamos cerca</div><h1>5 sucursales para <em>tus envíos</em>.</h1><div class="sub">Deslizá y encontrá la tuya →</div>'),
  f'<div class="slide feed" style="background:var(--g)"><img class="logo" src="{LOGO}"><div class="txt top" style="top:190px"><h2 style="font-size:84px">Nuestras sucursales</h2>{cards}</div></div>',
]

for k, v in {**H, **FEED}.items():
    write(k, v)
