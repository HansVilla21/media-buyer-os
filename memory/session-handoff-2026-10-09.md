# Handoff — 2026-10-09

> ⚠️ **HANDOFF HISTÓRICO — superado por `session-handoff-2026-10-10.md`**
> Se conserva como registro del estado al 2026-10-09. Para el estado actual, leer primero el nuevo.

**Estado al cierre:** en entrenamiento, con el material disponible completo. Claude Code se cerró
una vez durante el día (al terminar la sesión 18); al retomar se verificó en disco qué había
quedado y se completó lo que faltaba. Todo lo de abajo está escrito y verificado.

## Qué se hizo hoy

- Método de entrenamiento acordado con Hans y escrito en `CLAUDE.md`: cuatro capas (materia prima →
  apuntes → manual → skills «sin aplicar» hasta que se usen) y el ritual por sesión con autoexamen.
- Transcriptor local (`scripts/transcribe.py`, large-v3 int8 por lotes, GPU) y conversor de
  recursos (`scripts/convert_resources.py`). Las diez sesiones transcritas (2–9, 17, 18).
- **Diez sesiones procesadas**, cada una con apuntes, examen verificado contra la transcripción,
  manual y skills: índice en `knowledge/curso/indice.md`.
- **Manual:** 15 notas en `knowledge/manual/` (índice ahí). Choques resueltos y anotados: cuántos
  ads probar; link de calendario (nunca); acceso de clientes al Business Manager (parcial, nunca
  en el propio); automatización en LinkedIn (manual).
- **16 skills, todas «del curso, sin aplicar»:** diagnostico-de-cliente, escribir-ad-copy,
  grabar-y-revisar-el-ad, elegir-proceso-de-ventas, responder-dm-y-agendar, script-de-cierre,
  lanzar-campana-boost, definir-presupuesto, preparar-business-manager,
  lanzar-campana-business-manager, llevar-el-p-and-l, leer-los-numeros, evaluar-la-oferta,
  entregar-el-servicio, reporte-semanal, outreach-linkedin.
- **La oferta de Hans:** materia prima recogida (`output/diagnosticos/2026-10-09-materia-prima-oferta.md`)
  y tres candidatas contra las 6 preguntas (`output/diagnosticos/2026-10-09-ofertas-candidatas.md`),
  con la propuesta del media buyer: B (anuncios + sistema que atiende y agenda) como oferta, A
  (media buying puro) como primer paso; C (el sistema a medida tal como se vende hoy) no se pauta.
  **Pendiente: que Hans elija.**

## Decisiones de Hans del día (`memory/decisions.md`)

Desde cero de verdad; todo el curso aplica; sin formato preferido (video, él graba); mensajes
cortos y un paso a la vez; Hormozi y el documento OSO quedan en espera (Hormozi entró por el
recurso de la sesión 17).

## Lo que sigue, en orden

1. Hans elige candidata (A/B/C) → nicho → precio, garantía, capacidad (van al cerebro vía
   `output/para-cerebro/`).
2. `evaluar-la-oferta` sobre la elegida → `diagnostico-de-cliente` (17 preguntas, con Hans) →
   `escribir-ad-copy` → `grabar-y-revisar-el-ad` → validar con un solo video.
3. Antes de la primera campaña: guardrails por código en `.claude/settings.json` (con Hans) y
   `definir-presupuesto`.
4. Sesiones 10–16 cuando Hans las agregue (ahí debería estar «pausar y escalar» en detalle).

## Pendiente de Hans

- Los «ejemplos de ads ganadores para modelar» (sesión 4) son un link de Drive: hace falta el
  material descargado.
- Si mueve los videos de `C:\Users\hvill\Downloads\Media Buyer HQ\`, avisar.

## Aprendizajes del día (`memory/learnings.md`)

Transcripción por lotes sin condicionar en el texto anterior; la cola con descriptor aparte y
`/dev/null`; mensajes cortos para Hans; scripts de edición como archivo, no por heredoc; mirar el
peso de un recurso antes de imprimirlo (el `.md` de la sesión 18 pesa 988 KB por imágenes
incrustadas; pendiente separarlas en el conversor).
