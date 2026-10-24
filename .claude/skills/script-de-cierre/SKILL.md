---
name: script-de-cierre
description: Preparar el script de la llamada de ventas para quien cierra (Media Buyers HQ, sesión 5, Blueprints de Cierre): los diez pasos, las reglas, la oferta en tres partes, el precio y las objeciones, personalizados con la oferta y el ad copy. Hay versión genérica y versión para vender el servicio de media buying. Usar cuando una oferta va a salir a pauta con proceso a llamada, o cuando Hans va a vender su servicio. La llamada la toma Hans (o el cliente); el media buyer entrega el script y después lo ajusta con lo que pasó en las llamadas.
---

# Script de cierre

**Estado: del curso, sin aplicar** (sesión 5, 2026-10-09).

**Fuente:** `inputs/curso/recursos/Blueprint-de-Cierre-Script-de-Ventas.pdf.md` y
`Blueprint-de-Cierre-Servicio-Media-Buying.pdf.md` (texto completo). Manual:
`knowledge/manual/chat-y-llamada.md`. La llamada de venta es de Hans (`CLAUDE.md`).

## Qué entrega esta skill

Un documento `output/clientes/<cliente>/script-llamada.md` con los diez pasos escritos para esa
oferta, con las palabras del ad copy, listo para leer en voz alta. El curso lo personaliza con
este prompt (adjuntando el Blueprint): «Adjunto el Script de Ventas Genérico. Quiero que lo
adaptes a mi oferta, siguiendo exactamente los mismos pasos y la misma estructura. MI CONTEXTO:
mi nicho; mi oferta (qué vendo, qué incluye y qué resultado promete); precio y formas de pago;
garantía. AD COPY DE MI ANUNCIO. REGLAS: usa las palabras y problemas del ad copy en las preguntas
y en la presentación de la oferta; escribe las preguntas de situación, problema y meta
específicas para mi nicho; escribe la recomendación y la oferta completas para mi caso; agrega
las 5 a 8 objeciones más comunes de mi nicho, con la respuesta, usando la fórmula de 4 pasos;
trato de usted, frases cortas, fácil de leer en voz alta» `[CURSO S5 · Cierre, pp. 11–12]`. Acá lo
escribe el media buyer con el diagnóstico y el copy; quien cierra lo lee en voz alta y ajusta lo
que no suene a él.

## Los diez pasos `[CURSO S5 · Cierre, pp. 2–10]`

1. **Apertura** (1–2 min): ¿cómo está?, ¿de qué país y ciudad?
2. **Marco:** «le voy a hacer algunas preguntas para entender su situación… le voy a dar mi
   recomendación… y si veo que lo puedo ayudar, le doy más detalles de lo que yo ofrezco. ¿Le
   parece bien?» Esperar el sí.
3. **Situación:** ¿cuál es su situación actual con [tema]?
4. **Problema** (el más importante): ¿hace cuánto?, ¿qué ha intentado y cómo le fue?, ¿qué lo ha
   frenado?, ¿por qué cree que no ha funcionado?, ¿qué le está costando no resolverlo (dinero,
   tiempo, tranquilidad)?
5. **Meta:** si en 3–6 meses todo salió bien, ¿qué pasó?; ¿por qué es importante?; ¿por qué ahora?
6. **Resumen** con sus palabras: hoy está en…, lo frena…, le cuesta…, quiere llegar a… porque…
   ¿Es correcto? Urgencia del 1 al 10; menos de 7 → ¿qué haría que fuera un 10?; si no es
   prioridad, no se fuerza.
7. **Recomendación:** «le voy a decir lo que yo haría en su caso: primero…, después…, y con eso…».
   Útil aunque no compre.
8. **Oferta:** pedir permiso; «lo que yo hago es [una línea]. Funciona así: primero…, segundo…,
   tercero…. El resultado es que usted [su meta, con sus palabras]. ¿Alguna pregunta antes de que
   le diga la inversión?»
9. **Precio y cierre:** «la inversión es de [precio]». Silencio. Si no dice nada: «¿cómo lo ve?».
   Sí → link de pago ahí mismo y quedarse hasta que esté hecho.
10. **Objeciones:** validar → aislar → responder la real → volver a cerrar. Si no cierra: propuesta
    por WhatsApp y una fecha para hablar; nunca «yo le aviso».

## Reglas

La persona habla el 70 %. Anotar sus palabras. No presentar la oferta antes del paso 8 («con gusto
se lo digo, primero quiero entender su caso»). Después del precio, callarse. Cobrar en la llamada.
Decir la verdad: nada que no se pueda garantizar. Antes: leer el chat, tener precio y link listos,
conectarse 2 minutos antes con cámara, hoja para anotar.

## Versión para vender el servicio de media buying `[CURSO S5 · Cierre-MB]`

Cambian las preguntas (qué vende, a quién, a qué precio; cuántos clientes al mes y de dónde; si
corrió anuncios, cuánto y quién; quién atiende los mensajes; «¿qué pasa si los próximos 6 meses
siguen igual?»; capacidad), la recomendación (video ad → publicar en Instagram y Facebook con
[monto] al mes → responder rápido), la oferta (texto e instrucciones de grabación; publicar,
manejar y optimizar cada semana; reporte semanal), el precio («[precio] al mes, aparte el
presupuesto de anuncios directo a Meta»; referencia $500–1.500 en Latinoamérica; anclar: «con 3
clientes nuevos al mes se pagó solo») y las objeciones («ya probé anuncios», «yo le doy boost»,
garantía, presupuesto, tiempo, contrato mínimo de 3 meses, «¿con cuántos clientes ha trabajado?»
→ honesto, «mi sobrino me lo maneja»).

## En este proyecto (decisiones de Hans, 2026-10-11)

Con las dos ofertas de Hans, «cobrar en la llamada» y el link de pago del paso 9 no aplican tal cual:

- **Motor de Clientes:** no se cobra en la llamada (con el trato de prueba de los dos primeros, el
  cliente hoy no paga nada: `output/oferta/2026-10-15-llamada-josue-guion.md`, paso 3). Al sí, Hans le
  manda por WhatsApp el mensaje de confirmación (`output/oferta/2026-10-11-mensaje-confirmacion-motor.md`),
  el cliente responde «de acuerdo» y los pagos son por transferencia (`memory/decisions.md`, entrada
  «Motor: mensaje de confirmación en lugar de contrato; pago por transferencia»).
- **Sistemas a medida** (lo que pauta el copy 3): no se cierra en la llamada. Si dice sí, se agenda el
  diagnóstico; del diagnóstico sale el alcance y la cotización por escrito (núcleo desde USD 2.500 + IVA,
  lo propio de su negocio cotizado aparte); se cobra 50 % al arrancar y 50 % a la entrega aceptada
  (`output/oferta/2026-10-11-oferta-sistemas-a-medida-desde-cero.md`, «El camino, paso a paso»;
  `memory/decisions.md`, entradas «Sistemas a medida: pago 50/50 atado a la entrega aceptada…» y
  «Sistemas a medida: núcleo base USD 2.500, piso USD 1.500»). Si lo que el prospecto necesita es gente,
  Hans lo anota para cuando se paute el Motor (`output/oferta/2026-10-11-ad-copy-3-sistemas.md`, «Lo que
  esto mueve después de aprobarlo»). El guion de la llamada de sistemas está por escribir
  (`memory/tareas-activas.md`, paso 3).
- **Guion de Josué** (`output/oferta/2026-10-15-llamada-josue-guion.md`): **pendiente de reescribir antes
  del jueves 2026-10-15**, sin el nombre interno del producto y con los pasos de permiso y meta antes de
  la oferta (aviso en la cabecera del guion; auditoría, sección 4.11).

## Después de cada llamada

Quien cerró anota: resultado, objeciones que salieron, palabras del prospecto. Con eso se ajustan
el script, los templates de chat y, si hace falta, el copy. Se mide: llamadas → ventas.
