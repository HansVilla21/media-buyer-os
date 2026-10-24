---
name: leer-los-numeros
description: Leer los números de un ad o una campaña como enseña Media Buyers HQ (sesiones 6, 8 y 9): calcular las diez métricas desde el P&L, compararlas en pares (revenue por lead vs costo por lead, revenue por llamada vs costo por llamada, costo por venta vs precio), compararlas con la historia, y proponer seguir, subir, mantener o pausar. También proyecta escenarios antes de lanzar. Usar en cada revisión semanal, cuando Hans pregunta «¿va bien?», antes de pedir el OK para subir presupuesto o pausar, y antes de prometer cifras.
---

# Leer los números

**Estado: en prueba** (sesión 9, 2026-10-09; primera lectura real el 2026-10-17 con la campaña 1 de Hans, `output/clientes/hans/revisiones.md`). Mirar siempre también el desglose por ubicación y el paso de clics en el botón a conversaciones: ahí salieron las dos señales de la primera lectura.

**Fuente:** `knowledge/curso/09-key-metrics.md`, `08-algorithmic-targeting.md`,
`06-ad-campaign-ignition.md`; `inputs/curso/sesion-09-key-metrics/recursos/MB Ad Report.xlsx.md`.
Manual: `knowledge/manual/metricas.md`, `presupuesto.md`.

## Entradas

El P&L al día (skill `llevar-el-p-and-l`), el precio de la oferta, el presupuesto aprobado (skill
`definir-presupuesto`) y la historia: los números de los ads anteriores de esta cuenta.

## 1. Calcular `[CURSO S9 @ 0:17:15–1:11:02]`

Ad spend · revenue · leads (mensajes + opt-ins) · costo por lead · revenue por lead · llamadas ·
costo por llamada · revenue por llamada · ventas · costo por venta · profit · ROI. Si aplica:
conversion rates (DM → opt-in, lead → llamada, llamada → venta, lead → cliente) y lifetime value.
Las «revenue por…» no existen sin ventas: se dice.

## 2. Comparar en pares

- Revenue por lead **>** costo por lead → hay máquina; hasta cuánto se puede pagar por un lead.
- Revenue por llamada **>** costo por llamada.
- Costo por venta **<** precio (o < lifetime value). Con high ticket hay colchón.
- Si alguno falla con pocas ventas, no se concluye todavía: se mira el gasto contra el precio.

## 3. Comparar con la historia y con lo normal

- Costo por lead de esta cuenta en ads anteriores; costo por llamada; retorno. Un ad a 6 veces el
  costo por lead habitual «está malo» aunque sea rentable `[CURSO S9 @ 0:15:26]`.
- Sin historia (primeros ads): referencias del curso, marcadas como heurística: mensajes $1–3,
  llamadas $30–100, 1 % lead → cliente a lo largo del tiempo; si solo hay un ad, publicar otro
  para tener con qué comparar.
- Costo por mensaje estable al subir presupuesto = optimizando bien; costos que suben al escalar
  son normales si hay profit `[CURSO S8 @ 0:34:46]`, `[CURSO S9 @ 1:34:10]`.

## 4. Decidir (propuesta para Hans; nada se toca sin su OK)

| Situación | Propuesta |
|---|---|
| Profit y ROI positivos | seguir; subir de 10 en 10 (`definir-presupuesto`) |
| Sin ventas aún, costos dentro de lo normal, gasto < precio de la oferta | seguir: se está comprando data y los leads ya son profit; trabajar los leads (chat, llamadas) |
| Sin ventas, gasto ≥ precio de la oferta | pausar y proponer otro ad; antes, revisar si el problema está en el chat o la llamada (conversion rates) |
| Costo por lead/mensaje muy por encima de lo normal (×5 o más, o 7 días sin leads con objetivo correcto) | pausar ya; otro copy, más específico |
| Pierde consistentemente al escalar y no se puede salvar | pausar; volver al último presupuesto rentable o a otro ad |
| Leads que no califican | el copy (sesión 8), no la audiencia |
| Leads que no agendan | los mensajes del chat (`responder-dm-y-agendar`) `[CURSO S18 @ 0:55:57]` |
| Llamadas que no cierran | la llamada, el precio y la oferta (`script-de-cierre`, `evaluar-la-oferta`) `[CURSO S18 @ 0:55:57]` |
| Mes flojo con historia rentable | zoom out; seguir |

Siempre escribir qué se vio, con qué se comparó y por qué se propone eso. «Aquí no hay espacio
para las emociones» `[CURSO S9 @ 1:16:33]`.

## 5. Proyectar (antes de lanzar o de prometer) `[CURSO S9 · Ad Report]`, `[CURSO S9 @ 1:17:29–1:29:25]`

Leads = adspend ÷ costo por lead; clientes = leads × conversión; revenue = clientes × precio;
profit = revenue − adspend. Con $10/día presentar tres escenarios: costo por lead $1, $3 y $5–8,
con 1 % a lo largo del tiempo; el «bastante realista» es $3: 100 leads en 33 días por $333 y una
venta. Nunca prometer el de $0,50.

## Salida

Una nota corta en `output/clientes/<cliente>/revisiones.md` por revisión: fecha · ad · números
clave · pares · comparación · propuesta · OK de Hans (sí/no, fecha). Y al cliente, en su reporte
(sesión 17), con la regla de la sesión 2: cuánto se invirtió, cuánto se generó.
