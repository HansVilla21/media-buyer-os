---
name: definir-presupuesto
description: Calcular con el Protocolo Ad Budget de Media Buyers HQ (sesión 6) cuánto invertir en total para probar una oferta, cuánto por día y cuándo subir o parar, a partir del precio de la oferta, el capital disponible, la experiencia y la urgencia. Usar antes de lanzar cualquier ad, cada vez que se evalúa subir presupuesto, y cuando hay que decidir si un ad sigue o se pausa. Devuelve los números y la regla aplicada para que Hans apruebe el gasto.
---

# Definir el presupuesto

**Estado: del curso, sin aplicar** (sesión 6, 2026-10-09).

**Fuente:** `inputs/curso/recursos/Protocolo Ad Budget.md` y `knowledge/curso/06-ad-campaign-ignition.md`.
Manual: `knowledge/manual/presupuesto.md`.

## Entradas (las da Hans o el cliente)

- Precio de la oferta.
- Capital disponible para ads que no se necesita para vivir y que se está dispuesto a perder.
- Experiencia en ads de quien decide: baja, media, alta (con convicción en la oferta).
- Urgencia de comprar data: baja, media, alta.

## Cálculo `[CURSO S6 · Protocolo]`

1. **Total para probar el ad = precio de la oferta.** Si el capital es menor que el precio, se
   dice: «lo más probable es que vaya a correr ads con mucha presión económica»; se propone
   esperar a tener el mínimo o bajar el riesgo al máximo ($10/día).
2. **Diario:**
   - baja experiencia o poco capital → **$10/día** (capital ÷ 90);
   - media → capital ÷ 60 (≈ $15 con $1.000);
   - alta experiencia, alta convicción y urgencia → capital ÷ 30 (≈ $30 con $1.000; $60 con
     $2.000–5.000).
3. **Cuántos ads a la vez** (`[HEURÍSTICA derivada del curso]`): diario ÷ $10; principiante, 1–2.
4. **Duración de referencia:** el total ÷ el diario (en Boost, máximo 30 días por corrida).

## Reglas de seguimiento

- **Subir** solo con retorno positivo, en escalones: $10 → 20 → 30 → 40 → 50 → 100/día. Cada
  escalón pide OK de Hans.
- Con leads pero sin ventas: mismo presupuesto hasta la primera venta. Subir sin ROI+ solo para
  probar más ads distintos.
- **Parar:** gastó el precio de la oferta sin vender → pausa y otro ad. Vendió antes → sigue.
  Con números buenos (costo por lead, llamadas, demanda) se puede apostar hasta ~50 % más del
  precio por una venta `[CURSO S6 · FAQ]`. 7 días sin leads con objetivo correcto → mal ad.
- Siempre: ¿qué es lo peor que puede pasar? (se pierde el presupuesto de unos días) ¿y lo mejor?

## Salida

Un bloque en `output/clientes/<cliente>/campanas.md`:

```
Oferta: $X · Capital: $Y · Experiencia: … · Urgencia: …
Total para probar: $X · Diario: $Z · Ads a la vez: N · Días de referencia: X/Z
Regla de subida: con ROI+, $Z → … · Regla de parada: $X sin venta
Aprobado por Hans: AAAA-MM-DD
```
