# lancarg-redes

Repositorio público con las imágenes que se publican en las redes de Transportes Lancarg.
Metricool descarga cada imagen desde su link "raw" de GitHub. Acá va SOLO contenido que se publica: nunca datos internos.

## Antes de diseñar

- Leer la Guía de contenido (doc de Claude): https://claude.ai/code/artifact/da1707bc-728b-4f0f-b727-094289d8617d
  Ahí están el foco (paquetería chica), los valores, el tono, las reglas, los teléfonos y las ideas de formatos.
  Usar las frases de la sección "Frases y forma de hablar de Lancarg" y anotar ahí cada frase o corrección nueva de Fran.
  Para el feed, seguir la sección "Estilo de diseño para feed" (títulos en dos líneas blanco/rojo, franjas diagonales, títulos aprobados).
  ESTILO PRINCIPAL (Fran, 25-oct-2026): "foto real unida al diseño" para TODO (feed, historias y reels). NO usar más el fondo verde oscuro
  ni el degradado verde sobre fotos, ni el logo rojo y blanco. Siempre partes blancas con el logo a color (rojo y verde).
  Estilo favorito de Fran (oct-2026), usarlo seguido y variarlo: "foto real unida al diseño" (fondo blanco arriba con logo y título,
  foto que se funde con el blanco abajo, diagonales rojas/verdes en esquinas, sin tapar camiones). Estilo por defecto para publicaciones e historias.
  Bases: `publicaciones/ejemplo-foto-y-diseno/` (texto centrado), `ejemplo-foto-y-diseno-2/` (texto a la izquierda, espejado) y `2026-10-28-historia-foto-diseno/` (historia).
  Estilo "título sobre foto con caja roja": descartado por Fran (25-oct-2026), no usarlo.
- Logo: preferir SIEMPRE el logo a color, rojo y verde (`marca/versiones/1-principal-color.png`); a Fran no le gusta tanto el rojo y blanco (25-oct-2026).
  Sobre fondo blanco va directo; sobre foto, ponerlo en una zona blanca del diseño o en una pestaña blanca redondeada abajo al centro. `logo-lancarg-sobre-verde.png` (rojo y blanco) solo si no hay otra opción. No inventar otras versiones del logo.
- Fotos: nunca recortar personas ni camiones. En historias (9:16) las fotos horizontales van completas
  (object-fit: contain, centradas un poco arriba) sobre el fondo verde; ver `photo()` en plantillas/generar_semana_*.py.
- Vocabulario: decir "paquete/paquetes", no "caja"; "camiones" en plural (ej. "Camiones todos los días");
  "flota moderna" / "moderna flota" (ej. "Viaja en nuestra moderna flota").
  Rutas siempre con flecha doble ↔ (viajamos en los dos sentidos), nunca →.
- Reglas que no se rompen: nunca mencionar la cantidad de camiones, no inventar reseñas, no copiar a la competencia,
  no usar Higgsfield ni generadores pagos.

## Carpetas

- `fotos/` — fotos reales de la empresa (camiones, depósitos, cajas). Base de todos los diseños.
  - `fotos/vertical/` — versiones 9:16: usarlas primero en historias (llenan la pantalla, sin franjas).
  - `fotos/recortes/` — paquetes en PNG sin fondo para componer flyers libremente.
- `marca/` — logos. `logo-lancarg-sobre-verde.png` para fondos verdes o fotos; `logo-lancarg-color-transparente.png` para fondos claros.
  - `marca/logo-lancarg-vector-original.pdf`: el logo en vector que pasó Fran (CorelDRAW). Usarlo de base para todo lo nuevo.
  - `marca/versiones/`: principal, secundario (sin camión), simplificado (solo "Lancarg") e isotipo (solo el camión),
    cada uno en `-color` (fondos claros) y `-blanco` (verdes en blanco, para fondos verdes u oscuros), en SVG, PDF y PNG.
- `pedidos/` — imágenes que Fran crea a pedido (también puede subirlas a Drive, carpeta "fotos lancarg").
- `plantillas/` — `ejemplo-carrusel.html` (estilo de referencia) y `render.py`.
- `publicaciones/AAAA-MM-DD-tema/` — una carpeta por pieza: `diseno.html` + los JPG renderizados.

## Flujo semanal (lunes)

1. Revisar en Metricool (marca "Transporte Lancarg": página de Facebook "Transporte Lancarg" + Instagram @lancargsanjuan) qué hay programado y qué rindió.
2. Armar la semana: 4 publicaciones de feed (lunes, miércoles, viernes, domingo) y hasta 4 historias por día
   (sin contar publicaciones y reels compartidos en historias).
2b. Historias fijas, 3 veces por semana (martes, jueves y sábado), a las 12:00, 12:01 y 12:02 (esos días hay 1 historia más, total 4):
   `publicaciones/historias-fijas/` (estilo principal, oct-2026): sucursales `lancarg-1.jpg`, horarios `lancarg-2.jpg` y atención al cliente
   `lancarg-3.jpg` (se generan con `plantillas/generar_historias_fijas.py`). Se reutilizan esas mismas imágenes (no rediseñar salvo cambio de datos).
   El sticker de link a WhatsApp no se puede poner por API: va sin sticker.
3. Por cada pieza: `publicaciones/<fecha>-<tema>/diseno.html` con `.slide` de 1080x1350 (feed) o 1080x1920 (historia),
   renderizar con `python3 -I plantillas/render.py publicaciones/<carpeta>/diseno.html lancarg` y mirar cada JPG antes de subirlo.
4. `git add`, commit y push a `main`.
5. Programar en Metricool con `media` = `https://raw.githubusercontent.com/sanchez1francisco9-cpu/lancarg-redes/main/<ruta>`,
   providers facebook + instagram, zona horaria America/Buenos_Aires.
   - Horarios: consultar `getBestTimeToPostByNetwork` (instagram y facebook) para la semana y usar el mejor horario libre.
     Si el mejor horario de Instagram y el de Facebook no coinciden, programar por separado: un post solo para cada red,
     cada uno en su mejor horario (pedido de Fran). Referencia oct-2026: las dos redes pican a las 10:00;
     IG tiene otro pico a las 18:00 y FB a las 12:00; el fin de semana rinde la mitad.
   - Todo automático (historias, feed y reels): `autoPublish: true` y `instagramData.autoPublish: true`.
     Fran revisa antes en el calendario de Metricool y cambia o borra lo que no le guste.
   Las historias van sin texto.
3b. Reels animados (pedido de Fran, oct-2026): en el feed preferir reels animados para piezas con pasos o emotivas
   (ej. "El viaje de tu paquete", "Desde 1957"); los carruseles de consulta (sucursales) quedan como carrusel.
   `diseno.html` con `.scene` + `plantillas/motion.css` y `plantillas/motion.js` (ver ejemplos en `publicaciones/*-reel-*`),
   revisar con `python3 -I plantillas/render_video.py <html> --preview 2,5,9` y exportar sin `--preview` (genera `lancarg.mp4`).
   Programar con facebookData/instagramData type REEL. Música (solo Instagram): `instagramData.audioConfiguration.audioId`
   con un tema instrumental (sin voces, pedido de Fran) de la biblioteca comercial; buscar con un término (ej. "upbeat instrumental")
   y elegir de los candidatos uno con "(Instrumental)" en el título. Facebook sale sin música.
   Cierre de todos los reels: escena `class="scene end white"` (fondo blanco, spacer, frase opcional y pill de WhatsApp)
   + `window.OVERLAY` con `marca/logo-lancarg-animado-horizontal.mp4` (logo animado aprobado por Fran, 5 s), que
   `render_video.py` superpone al exportar (start = inicio de la escena + 0.35, x 0, y 563, w 1080).
5b. Videos de Fran (reels): se toman directo de su Drive pasando el link de Drive en `media`; el archivo tiene que estar
   compartido como "Cualquier persona con el enlace". No editar el video salvo que Fran lo pida.
6. Si una idea necesita una imagen que no existe, programarla con una foto alternativa y pedírsela a Fran en el resumen.
7. Mandar a Fran un resumen corto: qué quedó programado y cuándo, y las imágenes que hacen falta.
