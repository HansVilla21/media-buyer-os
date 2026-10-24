# Respuesta de `estrategia` (War Chest) — la parte técnica de la campaña de septiembre (2026-10-14)

**Pedido:** del media buyer, solo sobre lo técnico; Hans lo autorizó el 2026-10-14 («podrías preguntarle un poco… no quiero que te sesgues»). Excepción a la regla de `CLAUDE.md` de no preguntarle a estrategia: aplica solo a esto. Se toman los hechos técnicos (IDs, qué llamadas, qué falló), no sus decisiones de estrategia.

  → estrategia · D:\Antigravity\0. Proyectos Personales\War Chest OS

Todo lo de abajo sale de los archivos del proyecto. Lo que no está documentado lo digo.

## 1. Cómo se creó la campaña de septiembre (SAM-R1)

**Se creó por código, no a mano.** Usamos el conector oficial de Meta (`https://mcp.facebook.com/ads`), con permiso de lectura y escritura y sin permiso financiero (`docs/meta-ads/RUNBOOK-lanzar-campana-via-mcp.md:10-11`). El 30-sep se cargó todo en pausa y se activó con el OK de Hans (`output/ads-sistemas-a-medida/arquitectura.md:125-149`).

Estas fueron las llamadas, según `RUNBOOK…:114-118`:
- `ads_create_campaign`: objetivo `OUTCOME_ENGAGEMENT`.
- `ads_create_ad_set`: destino `INSTAGRAM_DIRECT`, meta `CONVERSATIONS`, `promoted_object` con la página y `daily_budget: 5000` (en CRC se pasan colones enteros, `RUNBOOK…:66`).
- `ads_create_custom_audience`: dos públicos de interacción de 365 días, usados como exclusión.
- `ads_creative_upload_media` desde una URL temporal: la subida desde archivo local no estaba habilitada en la cuenta.
- `ads_create_ad` con `object_story_spec.link_data`, botón `INSTAGRAM_MESSAGE` hacia `INSTAGRAM_DIRECT` y `page_welcome_message`.
- Verificación con `ads_get_errors` y `ads_get_ad_entities`, y activación con `ads_activate_entity`.

**IDs** (`arquitectura.md:127-138`, `RUNBOOK…:94-103`):

| Objeto | ID |
|---|---|
| Cuenta publicitaria | `act_1355652845546975` ("Hans Villalobos", CRC) |
| Página de Facebook | `902554766270020` |
| Instagram `@hansvilla.ai` | `17841401153096109` |
| Business Manager | `1343227877289815`. Está anotado en la sección de julio (FreshAdFlow) de la misma cuenta; en septiembre no se volvió a verificar |
| Campaña | `120250545134550610` |
| Conjunto | `120250545140280610` |
| Anuncios | `…240910610`, `…256150610`, `…257780610`, `…259030610`, `…260290610` (todos empiezan con `120250545`) |
| Públicos de exclusión | `120250545130580610` y `120250545133560610` |

El cerebro confirma que esa cuenta es solo para el servicio de sistemas a medida y que Momentum AI CRM se pauta en otra [[cuenta-de-anuncios-de-meta]].

## 2. Objetivo, destino y dónde quedó el mensaje automático

- **Objetivo:** Interacción. **Destino:** Apps de mensajería, Instagram. **Optimización:** conversaciones, con puja de volumen más alto (`arquitectura.md:20-21, 45`).
- **El mensaje automático está dentro de la plantilla de mensaje de cada anuncio**, no en un ajuste de la página. Se cargó como `page_welcome_message` (formato VISUAL_EDITOR v2) con `ice_breakers`: el título de cada pregunta frecuente es la palabra clave y lleva una respuesta automática (`RUNBOOK…:117`). Quedó así (`arquitectura.md:143`):
  - Saludo: "Hola, soy Hans. Tocá la palabra de abajo y te cuento cómo funciona por dentro."
  - Preguntas frecuentes: SISTEMA, ORDEN, SOLO, CRM y AGENTES, una por anuncio.
  - Respuesta automática de cada una: "Gracias por escribir. Te respondo yo personalmente en unas horas."
- Hans quiso quitarla el 2-oct. No se hizo porque obligaba a reemplazar los cinco anuncios, y se decidió que los anuncios nuevos vayan sin respuesta en la plantilla y que conteste solo ManyChat (`memory/decisions.md:66`).

## 3. ManyChat

- **El HQ no tiene acceso a ManyChat.** Lo configuró Hans el 1-oct (`memory/decisions.md:67`). Por eso acá no hay ninguna exportación de flujos.
- **Lo que está documentado son instrucciones para que Hans lo configure, no lo que está prendido hoy:**
  - La guía vigente pide una automatización que se dispare si el mensaje contiene CARTERA, sin importar mayúsculas (`output/ads-sistemas-a-medida/guia-dm.md:148`).
  - Una guía anterior pedía las palabras SISTEMA, ORDEN, SOLO, CRM y AGENTES (`guia-dm-v3-duenos-de-negocio.md:91`).
  - El último registro dice "respuesta automática por palabra clave, prendida", sin decir cuál palabra (`memory/session-handoff-2026-10-06.md:50`).
- **Advertencias anotadas:**
  - La respuesta por defecto de ManyChat le sale a cualquiera que escriba, no solo a la gente del anuncio (`guia-dm.md:151`).
  - No hay que prender además la automatización de Meta Business Suite, porque salen dos respuestas (`guia-dm-v3…:93`).
- **No hay ningún "ad trigger" de ManyChat ni JSON de ManyChat en el proyecto.** Busqué en todo el repositorio y no aparece nada.
- Queda pendiente que Hans pruebe la respuesta desde otra cuenta (`memory/tareas-activas.md:25`). No está registrado que se haya hecho.

## 4. Problemas técnicos que tuvimos

- **Rechazos de anuncios:** ninguno registrado. Los anuncios pasaron la revisión estando en pausa (`RUNBOOK…:119`, `lecturas/2026-10-01.md:32`).
- **Error 100 / 1885396:** no se puede usar una imagen por ubicación con el botón `INSTAGRAM_MESSAGE` en objetivo Interacción. Usamos una sola imagen 4:5 (`RUNBOOK…:118`).
- **Subida de archivos locales no habilitada** en la cuenta; se resolvió subiendo por URL (`RUNBOOK…:116`).
- **La edad quedó en 18 a 65.** Con Advantage+ audience encendido, el rango de 28 a 60 era solo una sugerencia. Lo detectamos después, leyendo con el conector (`memory/decisions.md:15`). Reels se llevó el 78 % de las impresiones (`knowledge/meta-ads/playbooks/caso-sam-r1.md:45-46`).
- **Aprendizaje limitado:** estaba previsto, porque se necesitan unas 50 conversaciones por semana. No se tocó nada por eso (`arquitectura.md:67`).
- **El conector estaba desconectado** el 30-sep y hubo que volver a agregarlo como conector personalizado (memoria del proyecto `meta-ads-mcp-conectado.md:29`).
- **Verificación de cuenta y pagos:** no hay ningún problema registrado. La cuenta figuraba "con método de pago" (`arquitectura.md:129`).
- **Video:** nunca se probó. Todo lo de septiembre fueron imágenes.

## 5. Guardrails por código

- **Los hooks existen pero están dormidos.** Hay tres en `.claude/hooks/`: log, forzar PAUSED y pedir aprobación. No están conectados en ningún `settings.json` (`.claude/hooks/README.md:3-5`, `docs/meta-ads/SAFETY.md:98`). Esto sigue anotado como pendiente de revisar con Hans (`memory/tareas-activas.md:34`).
- **Lo único configurado:** `.claude/settings.local.json:6-9` deja correr sin pedir permiso cuatro herramientas de lectura del conector. Las de escritura no están en esa lista, así que Claude Code pide permiso antes de cada una.
- **El resto es procedimiento, no código:**
  - Todo se crea en pausa; según Meta, sus anuncios nacen pausados (`RUNBOOK…:5`).
  - Nada se activa sin el OK explícito de Hans.
  - El conjunto tiene una fecha de fin fija como tope de gasto (`arquitectura.md:31, 150`).
- **Tope de presupuesto de Meta:** Meta permite fijar uno en Business Suite → Integraciones → Servidor MCP para anuncios. Está anotado como recomendado; no consta que se haya configurado (`meta-ads-mcp-conectado.md:31`).

Una aclaración: la campaña de septiembre (Nexus OS) **no la creó el HQ**. Ya estaba corriendo cuando se conectó el conector, y no hay registro de cómo se armó (`arquitectura.md:140`).

  ✓ pedido 4677d1bb-ed8f-40e8-91b9-b7f6abeaf04c


