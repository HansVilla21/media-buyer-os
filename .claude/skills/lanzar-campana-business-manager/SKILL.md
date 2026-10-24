---
name: lanzar-campana-business-manager
description: Crear y publicar una campaña de Meta (administrador de anuncios / Business Manager) de punta a punta, como se hizo con la campaña 1 de Hans el 2026-10-14. El media buyer arma campaña, conjunto y anuncio por la conexión con Meta, en pausa (video por link temporal, portada, texto, botón). Antes de entregar se revisa contra el curso con la lista de chequeo. Hans conecta ManyChat en la pantalla y publica, y después se verifica leyendo de vuelta. Trae las tres recetas de la sesión 7 (mensajes a Instagram, a WhatsApp, leads a página) y los errores conocidos con su arreglo. Usar para cada campaña o anuncio nuevo, de Hans o de un cliente.
---

# Lanzar una campaña en el administrador de anuncios

**Estado: en prueba.** Es del curso (sesión 7, 2026-10-09) y se usó por primera vez el 2026-10-14 con la campaña 1
de Hans. Salió publicada y sin errores, pero todavía no hay resultados. Pasa a **probada** cuando haya números de
esa campaña.

**Fuentes:**
- Curso: `knowledge/curso/07-meta-business-manager.md`, `[CURSO S7 @ 0:45:22–1:25:24]`.
- Manual: `knowledge/manual/business-manager.md`, `campanas.md` y `presupuesto.md`.
- La práctica: `output/clientes/hans/campana-1-plan.md`, `campanas.md` y
  `output/diagnosticos/2026-10-14-revision-campana-1-contra-curso.md`.
- **Lista de chequeo contra el curso:** `checklist-contra-curso.md`, en esta carpeta.

## Quién hace qué

| Paso | Quién | Dónde |
|---|---|---|
| Campaña, conjunto, subir video y portada, anuncio en pausa | media buyer | por la conexión con Meta |
| Revisión contra el curso y vistas previas | media buyer | conexión + `checklist-contra-curso.md` |
| Plantilla de mensaje con app de socio (ManyChat), mejoras automáticas apagadas, prender los tres niveles y publicar | Hans | pantalla del administrador |
| Verificar después de publicar y registrar | media buyer | conexión |

**OKs** (`CLAUDE.md`): el OK 1 de Hans es para cargar en pausa, y el OK 2 es publicar, que hace él mismo. Cada
cambio posterior pide su propio OK. Los guardrails de `.claude/settings.json` le impiden al media buyer activar,
editar, borrar o hacer Boost: **no se esquivan**, ni por la pantalla ni con otra herramienta. Son siete
herramientas y no cubren todo: píxeles, catálogos, experimentos y la edición de audiencias quedan fuera
(`memory/learnings.md`, 2026-10-23). Para esas vale igual la regla del OK.

## 0. Antes de cargar

- **Plata en la moneda de la cuenta:** el diario y el tope aprobados en dólares se convierten con el tipo de cambio
  de venta del BCCR del día, y la fuente se anota en `campanas.md`. La cuenta de Hans está en colones.
  (2026-10-14: se cargaron ₡5.000 «≈ $10» sin medir, y eran $11.)
- **El creativo, cerrado:** se releen los pendientes de su revisión. Se mide lo que se puede: duración (hasta 90 s
  para reels), música y peso.
  - Música: se compara el volumen en las pausas contra la versión sin música; hay una receta en
    `revision-campana-1-contra-curso.md` 1.1. El curso pide no usar música mientras se prueba
    `[CURSO S6 @ 0:14:17]`.
  - Si Hans decide otra cosa, se anota como decisión suya.
- **Chat listo:** textos del chat, quién contesta en menos de 5 minutos y, si hay ManyChat, la automatización en
  vivo (si no, no aparece en la pantalla).
- **Presupuesto aprobado** (skill `definir-presupuesto`).

## 1. Campaña

- **Objetivo:**
  - **Mensajes a Instagram, con un chatbot de terceros (ManyChat):** `OUTCOME_ENGAGEMENT` (Interacción). Es la
    variante de Hans.
  - **Mensajes a Instagram, sin bot:** Clientes potenciales, como en el curso `[CURSO S7 @ 0:50:31]`.
  - **WhatsApp:** Tráfico.
  - **Página:** Clientes potenciales.
- **Compra:** Auction. Sin categorías especiales, salvo crédito, empleo, vivienda o política.
- **Nombre:** «Campaign N – negocio – creativo». Va un video por campaña `[CURSO S7 @ 0:52:00–0:53:15]`.
- **Presupuesto de campaña por día**, con un solo conjunto y un solo anuncio `[CURSO S7 @ 0:55:04]`. Se agrega
  el tope total (`campaign_spend_cap`) con lo aprobado.

Así quedó la campaña 1:
```
ads_create_campaign: objective OUTCOME_ENGAGEMENT, buying_type AUCTION, campaign_daily_budget 5000 (CRC en
unidades enteras), campaign_spend_cap 150000, special_ad_categories "[]"
```

## 2. Conjunto

- **Nombre:** «Ad set N – país – género edad» `[CURSO S7 @ 0:57:45]`.
- **Destino:** `destination_type INSTAGRAM_DIRECT`, `optimization_goal CONVERSATIONS`,
  `billing_event IMPRESSIONS`, y `promoted_object {"page_id": …}` (la página de Hans es `902554766270020`).
- **Audiencia:**
  - Un país, sin intereses ni idioma.
  - Edad y género del avatar.
  - `targeting_automation.advantage_audience: 0`: sin esto, la edad es solo una sugerencia (septiembre salió de 18
    a 65). Es el «switch to original audience options» de la clase `[CURSO S7 @ 1:01:08]`.
- **Ubicaciones:** solo Instagram (`stream`, `story`, `reels`) con presupuesto bajo `[CURSO S8 @ 1:34:34]`. El
  curso, con más plata, suma los feeds de Facebook `[CURSO S7 @ 1:04:38]`.
- **Fin:** una fecha de fin como protección del gasto.
- **Ubicación (error #1870194):** al publicar, Meta rechazó el tipo de ubicación que puso sola
  (`frequently_in`, `home`) aunque se mandó solo el país. Después de recargar Costa Rica en la pantalla quedó
  `location_types ["frequently_in","home","recent"]`. `[SUPUESTO]` La próxima vez, pasar esos tres tipos de
  forma explícita al crear, y verificar que el error no aparezca.

## 3. Video y portada

- **Subida:** la cuenta **no acepta archivos desde la computadora** (`LOCAL_FILE`).
  - Se sube a un link temporal que se borra solo, con el OK de Hans: `curl -F reqtype=fileupload -F time=1h -F
    fileToUpload=@video.mp4 https://litterbox.catbox.moe/resources/internals/api.php`.
  - Después, `ads_creative_upload_media` con `URL` y `VIDEO`.
  - Se espera a que `ads_get_ad_videos` dé `ready`; tarda uno o dos minutos.
- **Portada:** se saca un cuadro del primer segundo con el hook en pantalla y los ojos abiertos (`ffmpeg -ss 0.2
  -frames:v 1`). Se sube igual, como `IMAGE`, y se usa su `image_hash`. Sin clickbait.

## 4. Anuncio

- **Nombre:** «Ad N – creativo – hook» `[CURSO S7 @ 1:06:31]`.
- **Creativo** de la campaña 1, en línea:
  ```
  {"object_story_spec":{"page_id":"…","instagram_user_id":"17841401153096109","video_data":{"video_id":"…",
  "image_hash":"…","message":"<texto corto con la palabra clave>","call_to_action":{"type":"INSTAGRAM_MESSAGE",
  "value":{"app_destination":"INSTAGRAM_DIRECT"}}}}}
  ```
- **Por defecto:** sin anuncios con otros anunciantes (`contextual_multi_ads` OPT_OUT) y sin mejoras automáticas.
  La declaración de IA solo vale en Europa, India, Taiwán, California y Nueva York, y se le menciona a Hans.
- **No se toca la plantilla de mensaje:** la conexión no puede elegir la app de socio. La elige Hans.
- **Video directo o post existente:** el curso acepta subir el video directo al anuncio o usar un post ya
  publicado `[CURSO S7 @ 1:08:38]`.

## 5. Antes de entregarle a Hans

1. Correr `ads_get_errors` sobre los tres niveles: tiene que salir vacío.
2. Revisar las vistas previas de cada ubicación: reels, feed e historias `[CURSO S6 @ 0:55:47]`. En el feed, el
   9:16 se recorta a 4:5: la cara y los subtítulos tienen que quedar adentro.
3. Repasar `checklist-contra-curso.md` punto por punto contra lo que se lee de vuelta en Meta. Lo que difiere
   del curso se le dice a Hans una vez, con el riesgo, y él decide.
4. Registrar en `output/clientes/<cliente>/campanas.md` los IDs y la configuración.

## 6. Lo que hace Hans en la pantalla (se le pasa así)

1. Abrir el anuncio → **Plantilla de mensaje → App de socio → ManyChat → la automatización**. Nada de saludo ni
   preguntas frecuentes de Meta.
2. En el anuncio, **«Advantage+ creative» / «Optimizaciones»: todo apagado.** Está a nivel de anuncio, no en el
   conjunto ni en la campaña.
3. **Prender los tres interruptores: campaña, conjunto y anuncio.** En la lista de conjuntos se mira el nombre:
   en la cuenta de Hans hay un conjunto viejo de Nexus OS prendido que confunde.
4. Si aparece «Revisar y publicar» con errores: «Corregir error» y mandar la captura. **Nunca «Intentar publicar
   elementos con errores».**

## 7. Después de publicar

- **Leer de vuelta los tres niveles:** `ACTIVE`, presupuesto, edad, Advantage+ de audiencia apagado y
  ubicaciones. Si Hans dice «prendido» y la lectura dice `PAUSED`, se esperan 60 segundos y se vuelve a leer. Si
  el `updated_time` no cambió, el clic no llegó: mirar en la pantalla qué está prendido.
- **«En preparación» y «En revisión» son normales:** Meta tarda horas en aprobar `[CURSO S6 @ 0:10:42]`.
- **Registrar** en `campanas.md` la hora de publicación y el creativo final. El creativo cambia cuando Hans
  conecta ManyChat.
- **Números:** skill `leer-los-numeros` desde el día siguiente. Reglas de parada en `campanas.md`:
  - **2 días sin mensajes:** revisar y proponer pausa `[CURSO S18 @ 0:31:25]`.
  - **7 días, o costo muy por encima de $1–3:** cambiar el hook.
  - **Gasté el tope sin venta:** las 6 preguntas.
  - **24 horas sin gastar:** esperar; después, recrear `[CURSO S6 · FAQ]`.
- **Rechazo por políticas:** pedir revisión; si no, otro anuncio `[CURSO S7 @ 1:45:49]`. Si es por la música,
  subir la versión sin música.

## Errores conocidos

| Error | Causa | Arreglo |
|---|---|---|
| «Local file upload is not available» | la cuenta no acepta archivos locales | link temporal + `URL` (paso 3) |
| #1870194 al publicar: «opción de segmentación por lugar que se eliminó» | tipo de ubicación viejo puesto por Meta | Hans recarga el país en Público → Ubicaciones; por código, ver paso 2 |
| Cada nivel dice que el otro está «desactivado» | falta prender un interruptor, o se prendió un conjunto viejo | prender los tres, mirando los nombres |
| La edad sale de 18 a 65 | Advantage+ de audiencia prendido | `advantage_audience: 0` |
| Imagen por ubicación con botón de mensaje de Instagram (100 / 1885396, War Chest) | Interacción no lo acepta | una sola pieza |
| Presupuesto «≈ $10» que no lo era | no se midió el tipo de cambio | convertir con el BCCR del día (paso 0) |

## Las recetas del curso por pantalla (cliente sin conexión)

**Campaña** `[CURSO S7 @ 0:48:41–0:57:01]`:
- Create → Auction → objetivo según el destino → Manual.
- Nombre estándar. Advantage campaign budget encendido con el diario del Protocolo.

**Conjunto** `[CURSO S7 @ 0:57:45–1:05:59]`:
- Conversión en Instagram, en WhatsApp (número verificado; sacar Messenger) o en sitio web (pixel y evento
  Lead).
- «Switch to original audience options»: un país, edad y género, sin intereses; «reach people beyond your
  detailed targeting» encendido; idiomas en blanco.
- Ubicaciones manuales: feeds, historias y reels. Sin in-stream, search, audience network ni marketplace.

**Anuncio** `[CURSO S7 @ 1:06:31–1:10:55]`:
- «Ad 1». Página e Instagram.
- «Use existing post» o subir el video.
- Multi-advertiser apagado. Botón «Send message», WhatsApp con su saludo guardado como plantilla, o «Learn
  more» con el link.

## Lo que no se hace

- Para empezar: nada de varios países, intereses, ubicaciones automáticas ni varios creativos en una campaña.
  Cada uno suma variables.
- Para probar otro creativo, otra campaña («Campaign 2 – …») con la misma configuración.
- No se activa, pausa, sube presupuesto, edita ni borra nada sin OK. Tampoco se esquivan los guardrails.
