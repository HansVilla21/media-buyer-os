---
name: entregar-el-servicio
description: El ciclo completo de entrega del servicio de media buying según Media Buyers HQ (sesión 17): del cierre a la llamada de diagnóstico, la carpeta compartida, los accesos a las cuentas del cliente, copy → revisión → grabación → revisión → campaña, y el ciclo test → números → reporte hasta retorno positivo, con las reglas de trato (sistema propio, todo ASAP, expectativas directas, no cobrar por número de ads). Usar cuando entra un cliente nuevo —Hans incluido—, y como mapa de en qué paso está cada cliente.
---

# Entregar el servicio

**Estado: del curso, sin aplicar** (sesión 17, 2026-10-09).

**Fuente:** `knowledge/curso/17-media-buyer-delivery.md`. Manual: `knowledge/manual/entrega-y-reporte.md`,
`servicio.md`. Esta skill ordena a las demás; cada paso tiene la suya.

## El ciclo `[CURSO S17 @ 0:14:50–0:29:07]`

| # | Paso | Skill / nota | Regla |
|---|---|---|---|
| 1 | Llamada de ventas; se cierra | `script-de-cierre` | **ahí mismo se agenda el diagnóstico** para el día siguiente. Motor: al sí, mensaje de confirmación en lugar de contrato (`output/oferta/2026-10-11-mensaje-confirmacion-motor.md`) |
| 2 | Llamada de diagnóstico, 45–60 min | `diagnostico-de-cliente` | en Zoom, notas en vivo en la carpeta compartida; pedir los accesos |
| 3 | Carpeta compartida (Google Drive) | abajo | una por cliente, compartida a nivel de carpeta; link directo en cada aviso |
| 4 | Ad copy | `escribir-ad-copy` | 90 s; AI y naturalizar |
| 5 | Revisión del cliente | `escribir-ad-copy` | que suene a él, no que apruebe copywriting |
| 6 | Instrucciones de grabación | `grabar-y-revisar-el-ad` | trípode, vertical, 90 s, fondo, cámara, audio |
| 7 | El cliente graba y sube | — | a la carpeta |
| 8 | Revisión del video | `grabar-y-revisar-el-ad` | lista de la sesión 4 |
| 9 | Campaña | `lanzar-campana-boost` o `lanzar-campana-business-manager`; `definir-presupuesto` | $10/día de base; **con OK de Hans** por cada escritura en Meta |
| 10 | Test → números → reporte, repetir | `llevar-el-p-and-l`, `leer-los-numeros`, `reporte-semanal` | hasta retorno positivo; los ads que haga falta |

**No se cobra por número de ads** `[CURSO S17 @ 0:27:52–0:29:07]`: se cobra retainer más
porcentaje y se prueban ads según el presupuesto hasta que uno funcione.

## La carpeta `[CURSO S17 @ 0:32:50–0:40:30]`

Google Drive, `<Nombre del cliente>/`: notas de llamadas · `Ad Copy N` · `videos/` · `imagenes/` ·
`testimonios/` · P&L · ventas desde ads. Compartir la carpeta entera al email del cliente. Copia de
trabajo local: `output/clientes/<cliente>/` (`diagnostico.md`, `ad-copy-N.md`, `campanas.md`,
`cuenta-meta.md`, `pnl.xlsx`, `revisiones.md`, `reportes/`). Con Hans, la carpeta local basta si
él no quiere Drive.

## Los accesos `[CURSO S17 @ 0:41:23–0:58:46]`

1. **Business Manager del cliente, acceso parcial** (People → email del media buyer → página y
   cuenta publicitaria → Send invitation). Siempre. Nunca sus ads en el Business Manager propio
   (`preparar-business-manager`).
2. **Boost desde su Instagram**, si el cliente lo elige sabiendo que implica credenciales o hacerlo
   él con instrucciones. Decirle: «mi reputación vale más que cualquier cliente; solo entro, mando el
   anuncio y salgo».
3. **Datos de ventas:** spreadsheet compartido (nombre, email, oferta, precio); analista en el
   procesador de pago o CRM; mensajes y ventas semanales del setter/closer.

Credenciales de clientes: **nunca** en un archivo de este proyecto ni en el chat (`CLAUDE.md`).

## Trato `[CURSO S17 @ 0:33:15–0:35:34, 1:03:21–1:12:30]`

- El media buyer pone su sistema; se adapta en lo razonable; no es un «sí a todo».
- Reporte semanal fijo + llamada mensual de 30–40 min + WhatsApp. Sin llamadas largas.
- Todo ASAP. Siempre en términos de resultados. Relación profesional.
- Expectativas claras y directas desde el inicio: primer mes de testeo, primeros mensajes en
  24–48 h, los ads que haga falta, qué hace cada quien (`servicio.md`).
- Leer a la persona: si no hay match de energía y expectativas, decirlo antes de cobrar.

## Registro

`output/clientes/<cliente>/estado.md`: en qué paso está, fecha de cada paso, accesos recibidos
(sin credenciales), próximos pasos y OKs de Hans pendientes.
