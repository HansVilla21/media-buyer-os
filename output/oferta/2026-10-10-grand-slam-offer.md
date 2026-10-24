# La Grand Slam Offer de Hans — «Llamadas que Llegan» (v1.1, 2026-10-10)

> ⚠️ **Corrección 2026-10-16:** las «respuestas de Josué» del 2026-10-10 que se usan acá las redactó Hans,
> no Josué: no son palabras de cliente. Van marcadas `[SUPUESTO de Hans, no de Josué]`. Lo que Josué dijo de
> verdad está en `output/diagnosticos/2026-10-15-llamada-josue.md`.

**Qué es este documento:** la oferta armada con los cinco pasos de $100M Offers y sus potenciadores
`[HORMOZI · Offers, pp. 74–131]`, con todo lo que Hans decidió el 2026-10-10
(`2026-10-10-oferta-v1-borrador.md`, `memory/decisions.md`) y las palabras del avatar que ya hay
(`../diagnosticos/2026-10-10-respuestas-josue.md`). Sirve para la llamada de ventas y para el chat; el
anuncio dice solo la punta (sección 10). Lo que es hipótesis va `[SUPUESTO]`; lo que es estimación,
`[ESTIMADO]`. Precio, garantía, plazo, capacidad y forma de pago: decididos por Hans.

---

## 0. La tarjeta

| | |
|---|---|
| **Para quién** | Dueños de un servicio de alto valor ($2.000–3.000 o más por cliente) en Costa Rica, que ya venden y cierran por llamada o WhatsApp. Primer anuncio: los que consiguen clientes por contenido, referidos y mensajes (ángulo A). |
| **Promesa** | «Llamadas con clientes que encajan, todas las semanas, sin que usted toque el marketing, y la certeza de qué anuncio los trae.» (segunda mitad aceptada por Hans el 2026-10-10, v1.1) |
| **Mecanismo** | Un sistema para conseguir clientes, escrito y medido con inteligencia artificial: anuncio de 90 s que el cliente graba → el copy filtra → chat que califica y agenda → seguimiento para que nadie se pierda → números cada semana. Nombre interno: «Llamadas que Llegan» (no se dice en público hasta que esté probado). |
| **Precio** | **$1.000 + IVA cada cuatro semanas** + 10 % de lo que el cliente cobra a cada cliente nuevo que entró por el anuncio (desde el día uno, mientras dure el servicio; hoja compartida semanal); mínimo tres meses **desde el primer mes pagado**; la pauta la paga el cliente a Meta desde $10/día; sin fee de setup. Pago por transferencia (decisiones del 2026-10-11, noche). |
| **Primeros dos clientes** | Mes de prueba: $0 hoy; $1.000 + IVA a los 30 días **desde que el anuncio sale al aire**, solo si llegaron **prospectos que encajen con los criterios del cliente** (graba en 7 días, contesta en menos de 5 minutos). Si no llegaron, no paga, y cualquiera sale sin costo o sigue otro mes igual. Por escrito: mensaje de confirmación (`2026-10-11-mensaje-confirmacion-motor.md`), no contrato. |
| **Garantía** | **GA (2026-10-11):** si en un mes pagado no le llegan prospectos **que encajen con sus criterios** (escritos en el diagnóstico del día 1; el media buyer clasifica cada conversación; el cliente tiene 5 días hábiles para objetar), el mes siguiente se trabaja gratis; **vale una vez**: si fallan dos meses seguidos, cualquiera termina. Condición: graba en 7 días, contesta en < 5 min, mantiene la pauta. Lo entregable, garantizado (G2). Nunca ventas. |
| **Cupo** | 5 clientes para empezar. |

**El molde `[HORMOZI · Offers, pp. 36–38]`:** la agencia de leads del libro pasó de «le manejo los
anuncios por $X al mes» a «pague una vez, nosotros cubrimos la pauta, paga solo si la gente llega,
garantizamos 20 personas o el mes siguiente gratis, y le regalamos el playbook»: 22,4× más caja. La
nuestra, punto por punto: pago ligado a que lleguen prospectos (P-C y GA), el cliente pone su pauta
(no la cubrimos: sin casos ni caja, sería irresponsable `[SUPUESTO]`), garantía de mes gratis, y los
bonos (guía, reactivación, playbook del nicho).

## 0b. El diferenciador (v1.1, 2026-10-10): un sistema que lee y aprende, no uno que habla

**El problema que Hans puso sobre la mesa:** «llamadas con clientes que encajan» lo promete cualquier
media buyer; «lo hacemos con IA» lo dice cualquiera, hasta Sebastián; y un chatbot no lo quiere la
gente. ¿Dónde está, entonces, lo que solo Hans puede ofrecer sin salirse de su experticia?

**Respuesta del media buyer:** no en lo que el anuncio promete (el resultado soñado es el mismo para
todos los competidores: eso dice Hormozi, se compite en probabilidad, tiempo y esfuerzo `[HORMOZI ·
Offers, p. 62]`) ni en un bot que habla, sino en **un sistema que lee**. Lo que un media buyer entrega
es el anuncio y un reporte de Meta. Lo que ninguno entrega, porque hay que construir software, es
esto:

1. **Leer cada conversación que trae el anuncio** y clasificarla con los criterios del cliente:
   calificado o curioso, en qué etapa quedó (contestó, calificado, agendó, llegó, compró), y **de qué
   anuncio vino**.
2. **Decirle al dueño, cada semana, qué anuncio le trae a los que compran**, no cuántos clics tuvo.
   Palabras de Josué: «yo vivo de medir, y hoy no puedo decirle qué campaña me trae a los buenos»;
   «no quiero gente curiosa».
3. **Devolverle a Meta la señal de quién calificó y quién compró**, para que el algoritmo traiga más
   de esos y menos curiosos. El curso lo nombra: «el pixel con datos de llamadas o ventas permite
   después optimizar a eso, alimentar el pixel» `[CURSO S8 @ 0:05:31–0:18:43]`; Felipe Carvajal lo
   hace con formularios `[COMPETENCIA · NuGen]`; nosotros, leyendo la conversación, sin formularios ni
   bot. Hans ya construyó esa pieza una vez: Momentum manda `QualifiedLead` y `Purchase` a Meta y
   está en producción en un negocio `[MENTOR CRM, 2026-10-10]`.

**Corrección con la investigación del 2026-10-11** (`../investigacion/2026-10-11-ia-y-adquisicion-de-clientes.md`,
§5): leer conversaciones de WhatsApp y devolver señales a Meta **no es tecnología inédita**: Meta lo
ofrece oficialmente (Conversions API para mensajería con `ctwa_clid` y evento `QualifiedLead`; «Automatic
Events» con regex + NLP para lead y compra) y varias herramientas lo hacen por reglas (Wati, Kommo,
respond.io, Chatfuel, Chatty en Argentina, Tintim en Brasil). **Lo que no existe:** un servicio en
español que lo venda como mecanismo con nombre; una IA que lea la conversación completa y decida
«encaja con la oferta» y «cuánto vale» sin frase gatillo; un reporte semanal anuncio → conversación →
llamada → venta escrito por IA para dueños de pymes; y nadie en Costa Rica. Y un riesgo nuevo: Meta
regala su propio «Business Agent» (junio 2026) y los Automatic Events, así que **el valor de Hans no
puede estar en el bot ni en «subir la campaña», sino en el criterio, la lectura de calidad y el
reporte** (investigación, §8.3). La frase correcta no es «ninguno lo entrega porque hay que construir
software» sino «lo que Meta construyó y casi nadie en Costa Rica cableó, leído con criterio».

**Por qué encaja con todo lo decidido:** es productizable (la misma lectura para todos, configurada
con los criterios de cada cliente); no es un chatbot (el cliente sigue contestando él; el sistema
lee, no habla: cero adopción); es la experticia de Hans de verdad (sistemas con IA sobre datos de un
negocio); le habla al que ya paga anuncios (ángulo B: «¿sabe qué anuncio le trae a los que compran?»)
y al que no (ángulo A: «desde el día uno va a saberlo»); y cierra el cuello de botella que el curso
señala, conseguir los datos de ventas del closer cada semana `[CURSO S17 @ 1:15:13–1:17:56]`.

**Cómo respeta «no se construye hasta tener ventas»:** la versión 1 es manual y la hace el media
buyer: lee las conversaciones (Instagram por Business Suite con el acceso del cliente; WhatsApp con
lo que el cliente comparta), las clasifica, las atribuye al anuncio y arma el reporte. La promesa es
cierta desde el día uno: «cada semana sabe quién le llegó y qué anuncio los trajo». La versión 2, con
2–3 clientes pagando, automatiza la lectura con IA y conecta las señales a Meta: **ese es el primer
sistema que se construye, antes que el panel.** `[SUPUESTO, propuesta del media buyer; decide Hans]`

**Qué cambia en la oferta si Hans lo acepta:**
- La promesa gana su segunda mitad: «Llamadas con clientes que encajan, todas las semanas, **y la
  certeza de qué anuncio los trae**.» La primera mitad es lo que buscan; la segunda es lo que nadie
  más les da.
- El mecanismo, en una frase: «un sistema que lee cada conversación que trae su anuncio, separa a los
  que encajan de los curiosos, y entrena al anuncio con los que compran». Nombre interno candidato,
  además de «Llamadas que Llegan»: **«Anuncios que Aprenden»** `[SUPUESTO]`. En público, sin nombre
  hasta que esté probado.
- Pieza 8 de la pila (sección 6) y un paso más en el camino del cliente (sección 10).

## 1. La ecuación de valor aplicada `[HORMOZI · Offers, p. 62]`

Valor = (resultado soñado × probabilidad percibida) ÷ (tiempo × esfuerzo y sacrificio).

| Variable | Dónde estamos | Qué la sube |
|---|---|---|
| **Resultado soñado** | Alto: «más clientes» es lo que todos buscan `[CURSO S17 · 6 Preguntas, p. 7]`; Josué: «quiero citas calificadas» | Decirlo en sus palabras: clientes que encajan, no curiosos; llamadas, no «leads» |
| **Probabilidad percibida** | **Baja: sin casos.** Es el punto flaco | P-C (paga solo si pasó), GA (mes gratis, una vez), mostrar el sistema funcionando en la llamada, decir los pasos y los plazos con exactitud, la credibilidad real (sistemas con IA para negocios reales) |
| **Tiempo hasta el resultado** | Corto: anuncio publicado a los dos días de recibir el video; primeros mensajes en 24–48 h `[CURSO S5 · Cierre-MB, p. 10]` | Decir los plazos; la victoria temprana son los primeros mensajes `[HORMOZI · Offers, p. 65]` |
| **Esfuerzo y sacrificio** | Bajo pero no cero: graba 90 s y contesta el chat (o su equipo) | Guía de grabación; templates de chat; el embudo de seguimiento que quita el «perseguir» |

La IA de Hans vive en el denominador: tiempo y esfuerzo `[HORMOZI · Offers, pp. 62–63]`. El
numerador se sostiene con la garantía hasta que haya casos.

## 2. Paso 1 — el resultado soñado `[HORMOZI · Offers, p. 79]`

Se vende el destino, no el vuelo: no «anuncios en Meta», sino «abrir el teléfono y encontrar mensajes
de gente que sí encaja, tener llamadas agendadas cada semana, y saber en números qué le trajo cada
dólar». Debajo: un negocio que no depende de su energía del día, que crece sin más horas ni más gente
`[CURSO S18 · Ad Copy]`, `[SUPUESTO de Hans, no de Josué]`, `[SUPUESTO]` para el ángulo A.

## 3. Paso 2 — todos los problemas, antes, durante y después `[HORMOZI · Offers, pp. 79–82]`

Cada problema es una razón para no comprar o para fracasar; se listan todos `[p. 88]`.

**Antes de empezar**
1. No sabe hacer anuncios y no tiene tiempo de aprender `[CURSO S18 · Ad Copy]`.
2. Miedo a perder plata en Meta `[SUPUESTO]`.
3. Miedo a que le lleguen «curiosos» sin con qué pagar `[SUPUESTO de Hans, no de Josué]`.
4. Ya le vendieron humo: agencias que prometen y no muestran nada `[SUPUESTO]`.
5. No sabe qué decir en un video ni le gusta la cámara `[SUPUESTO]`.
6. No sabe si su oferta está lista para pautarse `[CURSO S17 · 6 Preguntas]`.
7. No tiene configurada la cuenta publicitaria o el Business Manager, o la tiene mal `[CURSO S7]`.
8. No sabe cuánto invertir ni cuándo parar `[CURSO S6]`.

**Durante**
9. Le llegan mensajes y no sabe qué contestar ni cómo calificar `[CURSO S5 · Mensajes]`.
10. Contesta tarde (horas), y el lead se enfría `[CURSO S5]`.
11. Los que califican no agendan `[CURSO S18 @ 0:55:57]`.
12. Los que agendan no llegan a la llamada `[SUPUESTO de Hans, no de Josué]`.
13. En la llamada no cierra, o le dicen «tengo que pensarlo» `[CURSO S5 · Cierre]`.
14. No sabe qué anuncio o qué canal le trae a los buenos `[SUPUESTO de Hans, no de Josué]`.
15. No sabe si está ganando o perdiendo plata con la pauta `[SUPUESTO de Hans, no de Josué]`, `[CURSO S9]`.
16. El anuncio deja de funcionar y no sabe por qué (los ads tienen vida útil) `[CURSO S6 · FAQ]`.
17. Meta le rechaza el anuncio o le pide cosas `[OFICIAL pendiente]`.

**Después**
18. Los que no compraron hoy se pierden para siempre `[HORMOZI · Money Models, pp. 90–95]`.
19. Cuando funciona, no sabe cómo escalar sin romper lo que funciona `[CURSO S6]`, `[CURSO S9]`.
20. Le llegan más clientes de los que puede atender bien y se le desordena la operación (el dolor que
    hoy le resuelven los sistemas de Hans) `[DATO PROPIO]`.

## 4. Paso 3 — cada problema en una solución `[HORMOZI · Offers, pp. 80–84]`

| # | Problema | Solución (cómo…) | Pieza |
|---|---|---|---|
| 1, 5 | no sabe anuncios; no sabe qué decir | cómo tener el anuncio escrito y saber exactamente qué decir y cómo grabarlo en 90 s | copy con IA + guía de grabación |
| 2, 8 | miedo a perder plata; cuánto invertir | cómo probar con $10 al día y saber desde el día uno cuándo subir y cuándo parar | protocolo de presupuesto `[CURSO S6]` |
| 3 | curiosos | cómo que el anuncio le hable solo a quien puede pagar | copy que filtra (requisitos dichos) `[HORMOZI · lost chapter]` |
| 4 | humo | cómo ver todo: la campaña corre en su cuenta, con sus datos, y el reporte dice qué se gastó y qué trajo | campaña en su cuenta + reporte semanal `[CURSO S17]` |
| 6 | oferta sin probar | cómo saber si su oferta pasa antes de gastar un dólar | las 6 preguntas en el diagnóstico `[CURSO S17]` |
| 7 | cuenta mal armada | cómo dejar la cuenta lista sin tocar nada técnico | checklist de accesos y Business Manager `[CURSO S7]` |
| 9, 10 | no sabe contestar; contesta tarde | cómo contestar en menos de 5 minutos con una pregunta por mensaje, y calificar en 1–3 líneas | Blueprint de Mensajes + templates + una capacitación `[CURSO S5]` |
| 11, 12 | no agendan; no llegan | cómo que el que califica agende y el que agenda llegue | dos horarios + invitación + recordatorios 24 h y 2 h (embudo de seguimiento) |
| 13 | no cierra | cómo llevar la llamada con un guion y manejar «lo tengo que pensar» | script de cierre `[CURSO S5 · Cierre]` |
| 14, 15 | no sabe qué funciona ni si gana | cómo ver cada semana costo por mensaje, por llamada y por venta, y qué anuncio los trajo | P&L del curso + reporte semanal `[CURSO S7–S9]` |
| 16 | el ad se cansa | cómo tener siempre el siguiente ad probándose | variaciones y hooks nuevos cada ciclo `[CURSO S18]` |
| 17 | Meta rechaza | cómo escribir sin violar políticas y qué hacer si rechazan | revisión de políticas antes de publicar `[OFICIAL]` |
| 18 | se pierden los que no compraron | cómo volver a hablarles a las 2, 4 y 6 semanas sin perseguir | seguimiento del embudo |
| 19 | escalar | cómo subir presupuesto sin romper lo que funciona | protocolo de escalar `[CURSO S6, S9]` |
| 20 | se desordena la operación | cómo ordenar la operación cuando llegan más clientes | **otro servicio** (sistema a medida), upsell cuando aparezca `[HORMOZI · Money Models, pp. 71–73]` |

## 5. Paso 4 — cómo se entrega cada pieza `[HORMOZI · Offers, pp. 85–87]`

- **Hecho por Hans (DFY):** copy, campaña, optimización semanal, lectura de números, reporte. Es lo
  que el cliente no quiere hacer y lo que un «consultor de ads» no hace `[CURSO S6 @ 1:27:02]`.
- **Hecho con el cliente (DWY):** el chat y la llamada: templates, guion y una capacitación; lo opera
  su equipo o él. Se dice así, sin esconderlo `[CURSO S17 @ 1:10:40]`.
- **Uno a muchos (se hace una vez, sirve para todos)** `[HORMOZI · Offers, p. 89]`: guía de grabación,
  templates de chat, script, formato de reporte, protocolo de presupuesto, checklist de accesos, el
  embudo de seguimiento cuando se automatice.
- **Velocidad de respuesta:** anuncio publicado a los dos días de recibir el video; reporte cada semana; cambios ASAP
  `[CURSO S17]`.

## 6. Paso 5 — recorte y pila `[HORMOZI · Offers, pp. 88–91]`

Se queda lo de alto valor y bajo costo de entrega; lo caro de entregar (construir sistemas a medida,
operar el chat) sale del núcleo. La pila, con nombre para la llamada (los valores en dólares los pone
Hans si quiere mostrarlos; acá no se inventan `[ESTIMADO]`):

1. **El anuncio que filtra** — copy escrito con IA con la estructura del curso, tres hooks, guía de
   grabación de 90 s. *Resuelve 1, 3, 5.*
2. **La campaña en su cuenta** — montaje, $10/día del protocolo, optimización semanal, variaciones
   cuando el ad se cansa. *Resuelve 2, 7, 8, 16, 17, 19.*
3. **El chat que califica y agenda** — Blueprint de Mensajes, templates, una capacitación. *Resuelve 9,
   10.*
4. **El seguimiento que no pierde a nadie** — invitación, recordatorios 24 h y 2 h, seguimiento a los
   que no agendan y a los que no compran a las 2, 4 y 6 semanas. *Resuelve 11, 12, 18.*
5. **El guion de la llamada** — script de cierre del curso adaptado a su oferta. *Resuelve 13.*
6. **Sus números cada semana** — P&L (gasto, mensajes, llamadas, ventas, costo de cada uno) y reporte
   con comentarios. *Resuelve 4, 14, 15.*
7. **El diagnóstico de arranque** — las 17 preguntas y las 6 de la oferta, en una llamada al día
   siguiente del sí. *Resuelve 6.*
8. **La lectura de cada conversación** (v1.1) — cada mensaje que trae el anuncio, clasificado:
   encaja o curioso, en qué etapa quedó, de qué anuncio vino; cada semana, qué anuncio trae a los
   que compran; y, cuando se automatice, la señal de vuelta a Meta para que traiga más de esos.
   *Resuelve 3, 14, 15 de raíz, y hace posible el precio por resultado.*

Lo que se dice al final de la pila: «todo esto por $1.000 cada cuatro semanas, y usted pone la pauta
desde $10 al día». Referencia del mercado: media buying solo, $500–1.500/mes `[CURSO S5 · Cierre-MB, p. 8]`.

## 7. Potenciadores `[HORMOZI · Offers, pp. 97–131]`

- **Escasez (real):** 5 cupos. Se dice tal cual; cuando se llenen, lista de espera `[p. 106]`.
- **Urgencia (real, no inventada):** el trato P-C es solo para los dos primeros. Nada de «esta semana
  solamente».
- **Bonos** `[pp. 112–115]`: nunca se descuenta el núcleo; se agregan bonos, uno por obstáculo, en la
  llamada después de pedir la venta. Candidatos: **la guía de grabación** (obstáculo: la cámara);
  **reactivación de leads viejos** con templates (obstáculo: «ya tengo una base que no me contesta»);
  **el playbook del nicho**, cuando exista (copies que ya funcionaron en su rubro). Cada uno con
  nombre; valor en dólares si Hans quiere.
- **Garantía** `[pp. 119–125]`: para B2B high ticket, condicional y específica `[p. 120]`. La nuestra:
  GA (de servicio modificada: otro mes gratis, una vez `[p. 121]`) + G2 (lo entregable) + P-C para los dos
  primeros (pagá después solo si pasó `[HORMOZI · Money Models, pp. 58–60]`). Ponerle nombre a la
  garantía `[p. 119]`: candidato `[SUPUESTO]` «Garantía de Prospectos: si en 30 días no le llegan,
  el siguiente mes va por mi cuenta».
- **Nombre, M-A-G-I-C** `[pp. 126–131]`: imán (llamadas), avatar (dueños de servicios high ticket),
  meta (clientes que encajan), intervalo (cada semana; publicado a los dos días del video), contenedor (sistema).
  «Llamadas que Llegan» cumple cuatro de cinco (falta el intervalo en el nombre). **Queda interno**
  hasta que el método esté probado (Hans, 2026-10-10); en público se describe el sistema.

## 8. Precio y money model `[HORMOZI · Offers, pp. 49–56]`, `[HORMOZI · Money Models]`

- **El precio estándar del curso, con una pila premium** `[Offers, pp. 51–54]`: $1.000 + IVA es el centro
  del rango del curso para Latinoamérica ($500–1.500, `[CURSO S5 · Cierre-MB, p. 8]`); lo premium es la
  pila, la garantía y el 10 %, no el número.
- **Etapa I, atracción:** esta oferta; P-C como «pagá después» para los dos primeros `[Money Models,
  pp. 58–60]`; más adelante, un señuelo gratis (la guía o un video que enseña el sistema) + llamada
  `[Money Models, p. 148]`.
- **Etapa II, upsells cuando el reporte muestra el problema** `[Money Models, pp. 71–73]`: el chat con
  IA (Momentum) si «el chat me come el día»; el sistema a medida si «después del sí es un caos».
- **Etapa III, continuidad:** el servicio ya es mensual; cobrar cada cuatro semanas `[Money Models,
  p. 139]` ya está decidido; fee de setup condonado con compromiso `[p. 144]` queda para después.

## 9. Qué dice el anuncio y qué dice la llamada

| En el anuncio (90 s) | En el chat | En la llamada |
|---|---|---|
| filtro, promesa, quién habla, dolores, mecanismo descrito, CTA | calificar en 1–3 líneas; «¿por qué le interesó?»; dos horarios; invitación | la pila entera con nombres, los plazos, la garantía con nombre, el precio, P-C si es uno de los dos primeros, los bonos después de pedir la venta, el cupo |

Sin cifras con plazo ni garantía en el anuncio `[HORMOZI · Offers, p. 128]`; sin nombre del método
hasta que esté probado.

## 10. El camino del cliente, día por día (lo que entregamos y cuándo) `[CURSO S17 @ 0:14:50–0:29:07]`

| Cuándo | Qué pasa | Quién |
|---|---|---|
| Día −2 a −1 | El prospecto escribe al anuncio; en el chat se le piden sus últimas 20 conversaciones; en 24 h recibe la lectura (quién encajaba, quién no, por qué, dónde se perdieron); dos horarios para la llamada (decisión 2026-10-11) | media buyer |
| Día 0 | Llamada de ventas con la lectura en mano: la pila, el precio, la garantía GA; si dice sí, se agenda el diagnóstico para el día siguiente y se piden los accesos (Business Manager parcial, Instagram, hoja de ventas) | Hans |
| Día 1 | Diagnóstico de 45–60 min: las 17 preguntas y las 6 de su oferta; carpeta compartida creada; el cliente ve las notas escribirse | Hans + media buyer |
| Día 2 | Copy del anuncio (90 s), tres hooks, guía de grabación, en la carpeta; el cliente revisa que suene a él | media buyer |
| Día 3–5 | El cliente graba (celular, trípode, crudo) y sube el video; revisión con la lista del curso; templates de chat y guion de llamada entregados, con una capacitación de media hora | cliente; media buyer |
| Día 5–7 | Campaña al aire en su cuenta, $10/día del protocolo; revisión de políticas antes de publicar | media buyer, con el OK del cliente |
| Día 6–8 | Primeros mensajes (24–48 h). El cliente contesta en menos de 5 minutos con los templates; dos horarios e invitación; recordatorios 24 h y 2 h | cliente; el seguimiento, nuestro |
| Semana 2 y cada semana | Lectura de cada conversación (quién encaja, etapa, de qué anuncio); P&L y reporte semanal con comentarios; variación nueva si el ad se cansa; seguimiento a los que no agendaron o no compraron a las 2, 4 y 6 semanas | media buyer |
| Día 30 desde que el anuncio sale al aire | Corte: ¿llegaron prospectos que encajen con sus criterios? Para los dos primeros (P-C): si sí, paga $1.000 + IVA; si no, no paga y decide si sigue. Desde el primer mes pagado: si no llegaron, el mes siguiente gratis (GA, una vez). Llamada mensual de revisión | Hans |
| Mes 2–3 | Test → números → reporte hasta retorno positivo; con retorno, subir presupuesto con el protocolo; cuando aparece «el chat me come el día» o «después del sí es un caos», los upsells | media buyer; Hans |

## 11. Lo que le falta para ser Grand Slam de verdad

1. **Casos.** La probabilidad percibida se arregla con los dos primeros clientes (P-C). Hasta entonces,
   la garantía carga el peso.
2. **El nombre en público**, cuando el método se haya cumplido una vez.
3. **El embudo de seguimiento automatizado**, con 2–3 clientes pagando; hoy, plantillas y calendario.
4. **Las palabras de más avatares:** el doctor y 3–5 conocidos; hoy hay uno (Josué) y el copy del curso.
5. **Cubrir la pauta** como la agencia del libro: solo con caja y casos; no en la v1.
6. **La lectura automatizada y la señal a Meta** (sección 0b): manual en la v1; se construye con los
   primeros clientes.
