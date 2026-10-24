---
name: elegir-proceso-de-ventas
description: Decidir a dónde va la gente después del anuncio (Media Buyers HQ, sesión 5): entre los ocho procesos de venta del curso, escoger el correcto para una oferta y un negocio según si la oferta está probada, la experiencia del dueño, las habilidades de ventas, el presupuesto y la capacidad de atender mensajes y llamadas. Usar en el diagnóstico (pregunta 17) o cuando un cliente propone un funnel distinto. Devuelve el proceso, el CTA del ad y qué hay que tener listo.
---

# Elegir el proceso de ventas

**Estado: en prueba** (sesión 5, 2026-10-09). El proceso de la oferta de Hans se eligió con él en el
diagnóstico del 2026-10-10 (`output/diagnosticos/2026-10-10-diagnostico-oferta-v1.md`, pregunta 17):
anuncio → mensaje con palabra clave → chat que califica → lectura de sus conversaciones → dos horarios →
llamada. Pasa a «probada» cuando ese proceso tenga números de una campaña.

**Fuente:** `knowledge/curso/05-fusion-funnels.md`. Manual: `knowledge/manual/funnels.md`.

## Regla por defecto

Si hay duda, **el proceso más simple que tenga más contacto humano**: ad (60–90 s) → mensaje por
WhatsApp o Instagram → chat corto que califica y agenda → llamada → cierre `[CURSO S5 @ 1:07:56]`.
CTA del ad: «mándame un mensaje diciendo [palabra]».

## Las preguntas que deciden

| Si… | Entonces… |
|---|---|
| La oferta es nueva o no está probada con ads | el recomendado; es el que valida la oferta con un solo video `[CURSO S5 @ 0:53:22]` |
| El dueño es principiante en marketing y ventas | el recomendado: el contacto humano «salva el marketing» `[CURSO S5 @ 0:51:33]` |
| El presupuesto es bajo | el recomendado: menos clicks, proceso corto `[CURSO S5 @ 0:56:09]` |
| Quien chatea y cierra es bueno con la gente | el recomendado rinde más (8X vs 5X) `[CURSO S5 @ 0:22:11]` |
| Nadie puede responder mensajes en menos de 5 minutos ni tomar llamadas | hay que resolver eso antes de pautar, o pasar a ad → calendario directo (llamadas menos calificadas) `[CURSO S5 @ 0:17:25]` |
| El cliente ya tiene un VSL que vende y experiencia | ad → video → llamada (o → mensaje → llamada) `[CURSO S5 @ 0:27:14–0:28:39]` |
| El perfil de Instagram está muy optimizado y el cliente domina marca personal | se puede probar ad → perfil → stories → mensaje; si no, nunca `[CURSO S5 @ 0:12:18–0:13:00]` |
| Mucho volumen, buena facturación, quiere escalar sin equipo | opt-in + VSL + emails (+ link de pago si todo es excelente); la tecnología reemplaza la llamada `[CURSO S5 @ 0:56:37–1:00:22]` |
| Se pauta a Europa | verificar antes si Meta permite anuncios a mensajes segmentando ubicación; alternativa: ad → página con video y «mándeme un mensaje» `[CURSO S5 @ 1:16:16–1:20:24]` `[DATO DE ALUMNO]` |

## Qué tiene que quedar escrito

1. El proceso elegido, paso por paso, y por qué (cuál regla aplicó).
2. El CTA exacto del ad.
3. Quién responde los mensajes, en cuánto tiempo, y quién toma la llamada (es de Hans; con un
   cliente, su equipo).
4. Qué hay que tener listo antes de activar: templates de chat (skill `responder-dm-y-agendar`),
   script de llamada (skill `script-de-cierre`), calendario, link de pago; si hay página o video,
   quién lo hace y cuándo.
5. Qué se va a medir: costo por mensaje (referencia $1–3), mensajes → llamadas → ventas,
   invertido vs generado.

Se guarda en el diagnóstico del cliente (`output/clientes/<cliente>/diagnostico.md`, respuesta 17
y sección «Proceso de ventas»).

## En este proyecto: la lectura antes de la llamada (decisión de Hans)

La regla por defecto de esta skill es el proceso más simple con más contacto humano. Hans decidió
agregarle un paso: la lectura gratis de las últimas 20 conversaciones del prospecto, que se ofrece adentro
del chat solo a quien califica y le llega en 24 horas, antes de la llamada (`memory/decisions.md`,
entradas del 2026-10-11 «La entrada del servicio es una auditoría…» y «Ajustes al anuncio único…»).
**Manda la decisión de Hans.** Como agrega una variable a una oferta nueva (auditoría, panel de
jueces, `output/diagnosticos/2026-10-11-auditoria-oferta-y-anuncio.md`, líneas 71–72), se mide cuántas
lecturas terminan en llamada (la consecuencia que dejó la decisión) y, por separado, califican → mandan
→ agendan → llegan (C04, líneas 413–414). Con esos números se le muestra a Hans si la lectura sigue como
paso obligatorio o pasa a opcional; lo decide él.

## Lo que no se hace

- No se agregan landing, VSL ni emails a una oferta sin validar `[CURSO S5 @ 0:45:57]`.
- No se le recomienda a un cliente cerrar por chat `[CURSO S5 @ 1:14:00]`.
- Si el proceso ya funciona, no se toca: se escala `[CURSO S5 @ 1:27:58]`.
