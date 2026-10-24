---
name: llevar-el-p-and-l
description: Llevar el Profit & Loss de los ads con el spreadsheet del curso Media Buyers HQ (sesiones 7 y 8): qué se anota cada día o semana (clics, mensajes, optins, llamadas, ventas, gasto, revenue, fees, reembolsos), de dónde sale cada número, qué no se toca (las fórmulas) y cómo se lee (profit, ROI, costo por venta, con zoom out). Usar desde el primer día de una campaña activa, en cada revisión semanal, y para el reporte al cliente.
---

# Llevar el P&L

**Estado: del curso, sin aplicar** (sesiones 7 y 8, 2026-10-09).

**Fuente:** `inputs/curso/sesion-07-meta-business-manager/recursos/Profit & Loss Clients.xlsx`
(y su `.md` con las fórmulas) y `knowledge/curso/08-algorithmic-targeting.md`, sección 7. Manual:
`knowledge/manual/metricas.md`.

## Preparar

- Copia propia del spreadsheet por cliente: `output/clientes/<cliente>/pnl.xlsx` (o una hoja de
  cálculo compartida con el cliente). Hoja diaria y hoja semanal. **Las celdas «costo por…»,
  «revenue por…», profit y ROI son fórmulas: no se escriben.**
- Fee del procesador de pago según el que use el cliente (el curso pone 3,9 %).

## Qué se anota y de dónde sale `[CURSO S8 @ 1:00:46–1:12:43]`

| Columna | De dónde | Nota |
|---|---|---|
| Unique clicks | Ads Manager, «Unique link clicks» | con Boost no existe; se deja en 0 |
| Messages (DM) | conteo propio de mensajes que entraron desde el ad, o «Messaging conversations started» | Boost no lo da por día: contar |
| Optins | el software del funnel (Kajabi, etc.), no Meta | Meta cuenta de menos |
| Booked calls | el calendario, del evento de ese ad | pueden entrar días después |
| Sales | lo que reporta el cliente (spreadsheet, Stripe, CRM) | atribuir al día del lead o del cierre: «al final se suma todo» |
| Meta ad spend | Ads Manager, «Amount spent» del día | Google u otros, en su columna |
| Revenue | ventas cerradas | |
| Refunds | el cliente | |

Semanal: los mismos números sumados por rango de fechas.

Dos columnas que la sesión 9 agrega como fórmulas: **revenue por lead** (revenue ÷ leads) y
**revenue por llamada agendada** (revenue ÷ llamadas), para compararlas con costo por lead y costo
por llamada `[CURSO S9 @ 1:11:02–1:14:24]`. «Revenue por venta» no hace falta: es el precio.

## Cómo se lee `[CURSO S8 @ 1:12:43–1:22:28]`

- Lo único que manda: **profit** y **ROI**. Después, costo por venta, costo por llamada (en
  Latinoamérica $30–200, típico ~$50 `[HEURÍSTICA del curso]`), costo por mensaje ($1–3).
- **Zoom out:** no se decide con tres días; se mira por semana y por mes, y un mes flojo no pausa
  un ad que lleva meses rentable.
- **Gasto contra precio:** mientras no se haya gastado lo que cuesta la oferta, se sigue
  comprando data (`presupuesto.md`); con retorno positivo, la pregunta es cómo gastar más.
- El P&L mide los ads. Si el negocio no es rentable con buen retorno en ads, el problema es su
  estructura de costos, no la pauta.

## Ritual

- Diario (o cada dos días al inicio): anotar los crudos, 5 minutos.
- Semanal: cerrar la hoja semanal, calcular, decidir con la skill `definir-presupuesto` (subir,
  mantener, pausar) y proponer a Hans. Nada se cambia en Meta sin su OK.
- Al cliente: compartir la hoja; «los clientes son de números» `[CURSO S8 @ 1:41:44]`. El
  formato de reporte semanal llega con la sesión 17.
