# Métricas

Qué se mide, qué significa cada número y cómo se decide con ellos. Fuentes: sesiones 2, 5, 6, 7,
8, 9 y 18. Procedimientos: skills `llevar-el-p-and-l` y `leer-los-numeros`. El reporte semanal al
cliente: `entrega-y-reporte.md` y skill `reporte-semanal` (sesión 17).

**Última actualización:** 2026-10-09 (sesión 18).

## La métrica número uno

- Si genera más de lo que gasta: profit y retorno. «Gastamos 300 dólares en ads, hicimos una
  venta de 3 mil» `[CURSO S2 @ 1:14:22–1:15:54]`. «Sin profit no hay fiesta… profit es lo que
  paga las cuentas, no el revenue» `[CURSO S9 @ 1:00:52–1:15:17]`.
- CPC, CTR y «todos estos costos pequeños» no le importan al cliente `[CURSO S2 @ 1:15:01]`;
  revenue por clic «casi que no importa» `[CURSO S9 @ 1:14:24]`.
- Se invierte para «comprar data»: los números que permiten decidir. Se dice invertí, no gasté
  `[CURSO S9 @ 0:02:03, 0:11:09]`.

## Las métricas que se usan `[CURSO S9 @ 0:17:15–1:11:02]`

| Métrica | Cómo se calcula | Para qué |
|---|---|---|
| Ad spend | suma de lo invertido en los días | base de todo |
| Revenue | ventas brutas, antes de fees y de ads | base de las «revenue por…» |
| Leads | personas que mostraron interés: mensajes y opt-ins | volumen; Meta no cuenta mensajes como leads, el curso sí |
| Costo por lead | ad spend ÷ leads | si el mensaje conecta; bajo = más probabilidad, no garantía |
| Revenue por lead | revenue ÷ leads | hasta cuánto se puede pagar por un lead; **debe ser mayor que el costo por lead** |
| Llamadas | agendadas | — |
| Costo por llamada | ad spend ÷ llamadas | Latinoamérica $30–100 (hasta 200), típico ~$50 `[HEURÍSTICA]` |
| Revenue por llamada | revenue ÷ llamadas | **debe ser mayor que el costo por llamada** |
| Ventas | cerradas | — |
| Costo por venta | ad spend ÷ ventas | **debe ser menor que el precio** (o que el CLV) |
| Profit | revenue − ad spend − fees (− reembolsos) | lo único que manda |
| ROI | (revenue − invertido) ÷ invertido | se compara con la historia |
| ROAS | igual, solo sobre lo invertido en ads | lo mismo, más específico; poco usado |
| Conversion rate | acción ÷ paso anterior (DM → opt-in, lead → llamada, llamada → venta, lead → cliente) | toma sentido comparando |
| Customer lifetime value | lo que genera un cliente en 12 meses | para recurrentes y comisiones; invertir menos que eso por cliente |

- Las «revenue por…» no existen hasta la primera venta; por eso un ad con costos normales se
  deja hasta la primera venta, sin pasar el precio de la oferta `[CURSO S9 @ 0:40:19–0:41:13]`.
- Referencias del curso `[HEURÍSTICA del curso]`: costo por mensaje $1–3 (su ganador, $0,86 →
  $1,30 al escalar); 1 % de leads a clientes «a lo largo del tiempo» es realista (él ~4 % en high
  ticket sobre 13.000 leads); 20 % de cierre en llamadas en su ejemplo; 5–10 leads al día con $10
  en Latinoamérica.

## Cómo se decide `[CURSO S9 @ 0:15:26–0:17:15, 1:15:17–1:17:29, 1:29:25–1:31:56]`

- **Pares:** revenue por lead vs costo por lead; revenue por llamada vs costo por llamada; costo
  por venta vs precio. Si el primero es mayor, hay máquina; la pregunta pasa a ser cómo invertir
  más.
- **Perspectiva:** cada ad se compara con los anteriores; un costo por lead de $6 cuando la
  historia es $1 «está malo» aunque sea rentable. Al empezar se publican varios ads para tenerla.
- **No se pausa por miedo:** con costos dentro de lo normal se sigue hasta la primera venta o
  hasta invertir el precio de la oferta. Un costo absurdo (un mensaje a $30 en Latinoamérica) se
  pausa ya. «Aquí no hay espacio para las emociones.»
- **Al escalar los costos suben**; mientras haya profit, se sigue subiendo; se pausa cuando pierde
  consistentemente y no se puede salvar `[CURSO S9 @ 1:34:10–1:36:06]`.
- **Zoom out:** por semana y por mes; un mes flojo no pausa un ad con historia rentable
  `[CURSO S8 @ 1:15:34–1:17:25]`.
- Con un cliente: preguntar sus costos previos; acordar «un mes de testeo» `[CURSO S9 @ 1:42:34]`.
- **Dónde falla, qué se arregla:** sin leads → el ad copy; leads que no agendan → los mensajes;
  llamadas que no cierran → la llamada, el precio y la oferta `[CURSO S18 @ 0:55:57–0:56:23]`.

## Escenarios de referencia con $10 al día `[CURSO S9 @ 1:17:29–1:29:25]`

| Costo por lead | Leads/día | 100 leads en | Invertido | 1 % a $1.000 | Lectura del curso |
|---|---|---|---|---|---|
| $0,50 | 20 | 5 días | $50 | ~2.000 % | no realista al principio |
| $1 | 10 | 10 días | $100 | 1.000 % | más realista; no esperarlo |
| $3 | ~3 | 33 días | $333 | ~300 %, $670 profit | «bastante realista» |
| $5–8 | — | — | — | pérdida | — |

Proyección (modelo del `MB Ad Report`): leads = adspend ÷ costo por lead; clientes = leads ×
conversión; revenue = clientes × precio; profit = revenue − adspend `[CURSO S9 · Ad Report]`.

## Por qué el high ticket `[CURSO S9 @ 0:51:27–0:56:30]`

- Con $333 por venta, una oferta de $100 pierde y una de $1.000 gana; con $5.000 se puede pagar
  $2.000 por venta. «Cuando usted cobra high ticket, usted tiene un colchón gigante.»
- Salir tablas ya es ganancia: quedan los leads, que compran después. «Los leads ya son profit»
  `[CURSO S9 @ 0:56:30–1:00:18]`.

## Las columnas del Ads Manager (sesión 7) `[CURSO S7 · Columnas]`

Preset «Media Buyer Columns»: Campaign · Delivery · Reach · Unique link clicks · Cost per unique
link click · Landing page views · Cost per landing page view · Leads (website leads) · Cost per
lead · Messaging conversations started · Cost per messaging conversation started · Amount spent ·
Budget · CTR (link) · Impressions · CPM · Frequency.

Qué mide cada una `[CURSO S8 @ 0:53:30–0:58:56]`: Reach, cuentas únicas; Impressions, veces vistas;
Unique link clicks, un clic por persona; Landing page view, la página cargó y el pixel avisó;
Leads, opt-ins en la página; Messaging conversations started; CTR (link), no el «all»; CPM, entre
más bajo mejor; Frequency, veces por persona: a partir de 4, más ads. Los conteos de Meta se
contrastan con la fuente real: «no pongo mi mano al fuego por esta información».

## El P&L del curso `[CURSO S7 · P&L]`, `[CURSO S8 @ 1:00:46–1:15:34]`, `[CURSO S9 @ 1:11:02–1:14:24]`

Diario y semanal: clics únicos, mensajes, optins, llamadas, ventas, gasto, revenue, fees (3,9 %),
reembolsos; fórmulas: costo y revenue por mensaje, optin, llamada y venta; profit; ROI; y las dos
que suma la sesión 9: revenue por lead y revenue por llamada agendada. Solo se escriben los
crudos; leads contados en la fuente; llamadas desde el calendario; la venta al día del lead o del
cierre. El P&L de los ads mide los ads: si el negocio no es rentable con un 7X, el problema es su
estructura de costos `[CURSO S8 @ 1:25:02–1:30:27]`. Se le muestra al cliente.

## Referencia de costos del Boost de Sebastián `[DATO DEL CURSO]`

Tres creativos con todo igual: el mejor video, 80 conversaciones a $0,86 (luego ~300 a $1,27–1,30
con $50/día); el segundo, 11 a $2,34 (luego 25 a $3); un carrusel de texto, 4 a $4 (luego 30 a
$6) `[CURSO S7 @ 0:10:27–0:15:45]`, `[CURSO S8 @ 0:34:46–0:38:46]`, `[CURSO S9 @ 0:24:58–0:26:32]`.
Es su cuenta y su oferta: orden de magnitud, no meta.

## La meta es gastar más, no menos `[CURSO S8 @ 1:17:25–1:22:28]`

- Un 2X con $100 mil deja más profit que un 20X con $100. Con retorno positivo, la pregunta es
  «¿cómo gasto más?». Meta de ventas congruente con la inversión ($100 mil al mes con $20 mil en
  ads; $10 mil con $1.000 sí puede).
- Subir de 10 en 10: $10 → 20 → 30 `[CURSO S9 @ 1:40:09]`; «hay que invertir, pero no como locos:
  5, 10 dólares al día» `[CURSO S9 @ 1:42:34]`.

## Otras referencias

- «Followers don't pay the bills… lo que sí paga las cuentas son los leads» `[CURSO S6 @ 1:32:41]`.
- Primeros mensajes en 24–48 h; si no llegan, el ad o la oferta no son irresistibles
  `[CURSO S5 @ 1:39:52]`, `[CURSO S6 · FAQ]`.
- Rev share: ventas documentadas en spreadsheet, Stripe o CRM con acceso `[CURSO S6 @ 1:35:44]`.
- El contenido orgánico no es obligatorio, pero sube el retorno de los ads («nunca mató a nadie»)
  `[CURSO S9 @ 1:40:41–1:42:34]`.
