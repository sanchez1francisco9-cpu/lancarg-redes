"""Estilo principal de Lancarg (desde 25-oct-2026): "foto real unida al diseño".
Fondo blanco arriba con logo a color y título; foto real que se funde con el blanco abajo; diagonales rojas/verdes.
Uso: from estilo_blanco import page, story, feed  ->  page([story(...), ...]) devuelve el HTML completo.
"""
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#777;font-family:Inter,sans-serif}
.slide{width:1080px;position:relative;overflow:hidden;background:#fff;color:#02462D;margin-bottom:20px}
.story{height:1920px}.feed{height:1350px}
.photo{position:absolute;left:0;width:1080px;object-fit:cover}
.cut{position:absolute;left:50%;transform:translateX(-50%);filter:drop-shadow(0 30px 40px rgba(0,0,0,.25))}
.logo{position:absolute;left:50%;transform:translateX(-50%)}
.kick{position:absolute;left:50%;transform:translateX(-50%);background:#E70A0F;color:#fff;font-weight:800;font-size:34px;letter-spacing:.12em;text-transform:uppercase;padding:12px 26px;border-radius:4px;white-space:nowrap}
h1{position:absolute;left:30px;right:30px;text-align:center;font-family:"Inter Display",Inter;font-weight:900;line-height:1;letter-spacing:-.025em;text-transform:uppercase}
h1 .r{color:#E70A0F}
.bar{position:absolute;left:50%;width:140px;height:6px;background:#E70A0F;transform:translateX(-50%)}
.sub{position:absolute;left:40px;right:40px;text-align:center;font-size:38px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#1d2b25}
.sub b{color:#E70A0F}
.d{position:absolute;transform:skewX(-35deg);z-index:3}
.tr1{right:-120px;top:-20px;width:260px;background:#E70A0F}
.tr2{right:80px;top:-20px;width:100px;border:4px solid #E70A0F;border-top:0;border-bottom:0}
.br1{right:-170px;bottom:-10px;width:470px;height:200px;background:#E70A0F}
.br2{right:260px;bottom:-10px;width:100px;height:200px;background:#02462D}
.br3{right:420px;bottom:-10px;width:30px;height:200px;border-left:4px solid #E70A0F}
.feed .br1,.feed .br2,.feed .br3{height:180px}
.cta{position:absolute;right:50px;bottom:44px;text-align:right;color:#fff;font-weight:800;font-size:32px;line-height:1.25;z-index:4}
.cta small{display:block;font-size:26px;font-weight:600;opacity:.9}
"""
LOGO = "../../marca/versiones/1-principal-color.png"


def mask(a, b):
    g = f"linear-gradient(180deg,transparent 0%,transparent {a}%,rgba(0,0,0,.5) {(a+b)/2:.0f}%,#000 {b}%)"
    return f"-webkit-mask-image:{g};mask-image:{g}"


def slide(kind, photo=None, photo_top=0, photo_h=None, photo_pos="50% 50%", fade=(24, 38), cut=None, cut_top=0, cut_w=70,
          kick=None, title="", title_size=None, sub=None, top=None, cta=True, extra=""):
    H = 1920 if kind == "story" else 1350
    t = top or ({"logo": 260, "kick": 470, "h1": 540} if kind == "story" else {"logo": 70, "kick": 240, "h1": 300})
    size = title_size or (104 if kind == "story" else 92)
    lines = title.count("<br>") + 1
    h1_end = t["h1"] + int(size * 1.0 * lines)
    out = [f'<div class="slide {kind}">']
    if photo:
        ph = photo_h or (H - photo_top)
        out.append(f'<img class="photo" src="../../fotos/{photo}" style="top:{photo_top}px;height:{ph}px;object-position:{photo_pos};{mask(*fade)}">')
    if cut:
        out.append(f'<img class="cut" src="../../fotos/recortes/{cut}" style="top:{cut_top}px;width:{cut_w}%">')
    th = 190 if kind == "story" else 140
    out.append(f'<div class="d tr1" style="height:{th}px"></div><div class="d tr2" style="height:{th}px"></div>')
    lw = 560 if kind == "story" else 420
    out.append(f'<img class="logo" src="{LOGO}" style="top:{t["logo"]}px;width:{lw}px">')
    if kick:
        out.append(f'<div class="kick" style="top:{t["kick"]}px">{kick}</div>')
    out.append(f'<h1 style="top:{t["h1"]}px;font-size:{size}px">{title}</h1>')
    out.append(f'<div class="bar" style="top:{h1_end + 26}px"></div>')
    if sub:
        out.append(f'<div class="sub" style="top:{h1_end + 60}px">{sub}</div>')
    out.append(extra)
    out.append('<div class="d br1"></div><div class="d br2"></div><div class="d br3"></div>')
    if cta:
        out.append('<div class="cta"><small>Cotizá por WhatsApp</small>264 454-3612</div>')
    out.append('</div>')
    return "\n".join(out)


def story(**k): return slide("story", **k)
def feed(**k): return slide("feed", **k)


def page(slides):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>\n' + "\n".join(slides) + "\n</body></html>"
