"""Historias fijas (martes, jueves y sábado 12:00/12:01/12:02) con el estilo principal.
lancarg-1 sucursales, lancarg-2 horarios, lancarg-3 atención al cliente.
Uso: python3 -I plantillas/generar_historias_fijas.py && python3 -I plantillas/render.py publicaciones/historias-fijas/diseno.html lancarg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo_blanco import page, story

WA = '<svg width="38" height="38" viewBox="0 0 24 24" fill="#25D366" style="flex:none"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg>'
PIN = '<svg width="34" height="34" viewBox="0 0 100 100" style="flex:none;margin-top:6px"><path d="M50 8C33.4 8 20 21.2 20 37.6 20 60 50 92 50 92S80 60 80 37.6C80 21.2 66.6 8 50 8Z" fill="#E70A0F"/><circle cx="50" cy="37.5" r="12.5" fill="#fff"/></svg>'
CLK = '<svg width="34" height="34" viewBox="0 0 100 100" style="flex:none;margin-top:6px"><circle cx="50" cy="50" r="38" fill="none" stroke="#E70A0F" stroke-width="10"/><path d="M50 28V50L64 60" fill="none" stroke="#E70A0F" stroke-width="9" stroke-linecap="round"/></svg>'
CARD = 'display:flex;gap:20px;border:3px solid #e3e8e5;border-left:10px solid #E70A0F;border-radius:18px;padding:22px 28px;margin-top:20px;background:#fff'

SUC = [("San Juan", "Ruta 40 545 Norte, Chimbas", "264 454-3612"),
       ("Mendoza", "Mitre 2671, Guaymallén", "261 240-6204"),
       ("Buenos Aires", "Pergamino 3751, C.T.C. Villa Soldati,<br>Nave C, Módulo 75", "11 3779-5919"),
       ("Córdoba", "La Cordillera 3774", "351 311-2698"),
       ("Rosario", "Río de Janeiro 2510", "341 364-0498")]
LV16, SAB, LV17 = "Lunes a viernes de 8 a 16 h", "Sábados de 8 a 12:30 h", "Lunes a viernes de 8 a 17 h"
HOR = [("San Juan", [LV16, SAB]), ("Mendoza", [LV16, SAB]), ("Buenos Aires", [LV17]), ("Córdoba", [LV16, SAB]), ("Rosario", [LV17])]

suc = "".join(f'<div style="{CARD}">{PIN}<div><div style="font-size:42px;font-weight:900;color:#02462D">{n}</div>'
              f'<div style="font-size:30px;font-weight:500;color:#4a524e;margin-top:4px;line-height:1.25">{a}</div>'
              f'<div style="display:flex;align-items:center;gap:10px;font-size:38px;font-weight:800;color:#02462D;margin-top:8px">{WA}{t}</div></div></div>'
              for n, a, t in SUC)
hor = "".join(f'<div style="{CARD}">{CLK}<div><div style="font-size:42px;font-weight:900;color:#02462D">{n}</div>'
              + "".join(f'<div style="font-size:33px;font-weight:500;color:#4a524e;margin-top:4px">{x}</div>' for x in hs) + '</div></div>'
              for n, hs in HOR)
T = {"logo": 150, "kick": 0, "h1": 330}

slides = [
    story(title='Nuestras <span class="r">sucursales</span>', title_size=74, top=T, cta=False,
          extra=f'<div style="position:absolute;left:70px;right:70px;top:470px">{suc}</div>'),
    story(title='Nuestros <span class="r">horarios</span>', title_size=88, top=T, cta=False,
          extra=f'<div style="position:absolute;left:70px;right:70px;top:470px">{hor}'
                f'<div style="text-align:center;font-size:34px;font-weight:700;color:#02462D;margin-top:34px">Cotizaciones por WhatsApp: <b style="color:#E70A0F">264 454-3612</b></div></div>'),
    story(photo="chica-respondiendo-whatsapp.jpg", photo_top=1000, photo_h=1280, photo_pos="50% 30%", fade=(6, 20),
          title='Atención al cliente<br><span class="r">y cotizaciones</span>', title_size=86, top={"logo": 230, "kick": 0, "h1": 450}, cta=False,
          extra='<div style="position:absolute;left:0;right:0;top:680px;text-align:center;z-index:4">'
                '<div style="font-size:40px;font-weight:700;color:#1d2b25">Escribinos y te respondemos por WhatsApp</div>'
                f'<div style="display:inline-flex;align-items:center;gap:20px;margin-top:26px;background:#02462D;color:#fff;font-weight:900;font-size:74px;padding:22px 56px;border-radius:999px;box-shadow:0 14px 34px rgba(0,0,0,.2)">{WA.replace("38","64")}264 454-3612</div>'
                '<div style="font-size:32px;font-weight:700;color:#4a524e;margin-top:24px">Lunes a viernes de 8 a 16 h · Sábados de 8 a 12:30 h</div></div>'),
]
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "publicaciones", "historias-fijas")
open(os.path.join(d, "diseno.html"), "w").write(page(slides))
