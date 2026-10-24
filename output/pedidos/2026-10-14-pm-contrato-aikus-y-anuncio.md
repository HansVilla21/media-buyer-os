# Respuesta de `pm` — el contrato de AIKUS frente al anuncio de sistemas (2026-10-14)

**Pedido:** del media buyer, el 2026-10-14, por el canal entre departamentos (solo lectura). Hans preguntó si vender por anuncio el mismo tipo de sistema que se le construye al doctor puede generar un problema con su servicio.

  → pm · D:\Antigravity\0. Proyectos Personales\Momentum PM OS

# Qué dicen los documentos de AIKUS sobre el anuncio

**Conclusión:** en lo que hay en disco no encontré nada que le impida a Hans vender el mismo tipo de sistema a otros negocios, clínicas incluidas. El riesgo real está en lo que el anuncio muestre o cuente de AIKUS, no en que ofrezca el sistema. No soy abogado, así que esto es lectura del contrato y no una opinión legal.

**Antes de seguir:** no encontré una copia firmada. El PDF para firmar tiene las líneas de firma vacías (`Contrato-AIKUS-Fase-1.pdf`, p. 12 y 15). Además, el plan local se contradice: marca la firma como pendiente y el anticipo como pagado (`outputs/planes/plan-de-trabajo-aikus.html:624` y `:632`). Todo lo de abajo sale de ese texto. La versión que vale es el PDF (`contrato-aikus-fase-1.md:4`). En adelante, `contrato.md` es `momentum-ai-pm-os/clients/dr-carlos-hernandez/contrato-aikus-fase-1.md`.

## 1) Confidencialidad (Sección VIII y Anexo A)
- **Qué se considera confidencial:** la información de cada parte, por ejemplo «fórmulas, metodologías, procesos, prácticas competitivas, estrategia comercial, protocolos, "know-how"», precios y planes de mercadeo. Solo cuenta lo que no es público y se conoció por la relación (`templates/contratos/generador/build.js:357`; PDF p. 13).
- **Pacientes:** todos sus datos, incluidos los de salud, son confidenciales de forma expresa (`build.js:358`).
- **El acuerdo corre para los dos lados.** Los procesos de AIKUS son confidenciales para Hans, y la metodología de Hans también lo es para AIKUS.
- **Plantillas, configuraciones y diseño del sistema:** ninguna de esas palabras aparece. Por la definición, sí quedan cubiertos:
  - el proceso de AIKUS, por ejemplo su Camino del cliente
  - su plantilla de contrato, que la aporta el cliente (`contrato.md:36`, `:188`)
  - sus reglas de comisión
- **Excepciones:** no es confidencial lo que una parte ya sabía antes de firmar, ni lo que desarrolló sin usar información de la otra (`build.js:370`, `:373`). Esas excepciones no aplican a los datos de pacientes (`build.js:374`).
- **Obligaciones de Hans:**
  - no usar esa información en beneficio propio (`build.js:363`)
  - no hablar de ella con terceros sin permiso escrito (`build.js:364`)
  - no presumir de tenerla (`build.js:365`)
- **También son confidenciales los términos del contrato y su negociación** (PDF p. 10, Sección VIII).
- **Plazo:** dura toda la relación y hasta 4 años después de terminarla. Para los datos de pacientes no vence nunca (`build.js:380`; `contrato.md:204`).
- **Si se incumple:** se paga el daño completo, incluido el daño a la reputación (`build.js:381`). Una divulgación a propósito queda fuera del tope de responsabilidad (`contrato.md:198`).

## 2) Exclusividad o no competencia
- **No hay ninguna cláusula** que le impida a Hans ofrecerle el sistema a otros negocios, ni a otras clínicas.
- El contrato incluso dice que Hans no está sujeto a exclusividad (PDF p. 11, «Partes independientes»; `contrato.md:220`).
- La única cláusula de no contratar es sobre el personal de la otra parte, por 12 meses (`contrato.md:222`).
- La prohibición de comercializar el sistema es para el cliente, no para Hans: «El Cliente no podrá revender, sublicenciar ni comercializar el Sistema a terceros» (`contrato.md:163`).

## 3) Código y reutilización
- **Lo de AIKUS:** con el pago total es dueño del sistema implementado y de sus datos. Con el pago final recibe el código completo, con licencia perpetua «para su propia operación» (`contrato.md:159`, `:161`).
- **Lo de Hans:** conserva sus componentes preexistentes o de uso general, con «el derecho a reutilizarlos en otros proyectos» (`contrato.md:163`). Esa división se decidió a propósito el 22 de setiembre (`contrato.md:247`).
- **En la práctica:** el diseño ya reutiliza la firma electrónica de Grandir y las comisiones por producto y rol del CRM de Josué (`outputs/planes/plan-de-trabajo-aikus-interno.md:106`).

## 4) ¿Se le prometió que era único?
- **Por escrito no encontré esa promesa.**
- La propuesta promete que es suyo, no que es único: «el sistema queda de ustedes» y «el sistema es suyo» (`outputs/propuestas/propuesta-aikus-2026-09-22.html:421`, `:485`).
- El contrato habla de un «sistema propio de operación», pero como descripción de lo que el cliente necesita (`contrato.md:22`).
- **En llamadas:** solo hay dos registros en disco, `fuentes/2026-09-21_llamada-tania.md` y `fuentes/2026-09-02_camino-del-cliente-tania.md`. Ninguno dice nada parecido. De la reunión del 30 de setiembre no hay transcripción, así que lo que se dijo ahí solo lo sabe Hans.

## 5) Permiso para usarlo de referencia
- **No hay ningún permiso.** No aparece referencia, testimonio, caso ni portafolio en el contrato ni en los documentos del cliente.
- Por las cláusulas del punto 1, nombrar a AIKUS o mostrar sus pantallas, procesos o números necesitaría su autorización por escrito (`build.js:364`).

## 6) Estado y carga hasta la entrega
- **Fechas** (`ARRANQUE-desarrollo.md:11`; `plan-de-trabajo-aikus-interno.md:64-69`):

| Hito | Fecha |
|---|---|
| Arranque | 5 oct |
| Demo de la Tanda 1, con pacientes reales | viernes 16 oct (en 2 días) |
| Entrega | lunes 2 nov |
| Fin de la revisión | 9 nov |
| Fin del mes de soporte y de las plataformas pagadas por Hans | 2 dic |

- **Dónde corre:** desde el 12 oct está publicado en `aikus-sistema.vercel.app` (`ARRANQUE-desarrollo.md:5`).
- **Horas:** Hans estimó 87 h más 15 a 20 de migración. La auditoría calculó el mismo alcance en 165 a 200 h, con otros clientes en paralelo (`plan-de-trabajo-aikus-interno.md:75`).
- **Falta el avance real.** El estado de cada parte vive en `memory/backlog.md` del proyecto de desarrollo (`ARRANQUE-desarrollo.md:61`). No lo consulté por la regla de no leer memoria fuera del cerebro. Hans tiene que confirmar cuánto falta.

## Lo que hay en el cerebro
No tiene nada sobre el contrato de AIKUS. Lo más cercano, según el índice (no contestan la pregunta):
- [[clausula-de-llaves]]: cuentas a nombre del cliente y cero permanencia, escrito en el contrato.
- [[no-contar-como-trabajan-los-clientes-actuales]]: en un gremio cerrado, contar cómo trabaja un cliente vuelve como sospecha.
- [[no-decir-el-porcentaje-de-reutilizacion]]: decir cuánto ya estaba hecho invita a pedir descuento.

## Para el anuncio
Vender las funciones genéricas encaja con la cláusula de reutilización. Lo que el anuncio no debería hacer sin permiso escrito del doctor:
- nombrar a AIKUS o decir «se lo hice a un médico»
- mostrar sus pantallas o datos reales
- usar su proceso de cinco productos

Si Hans quiere usarlo como caso, conviene pedirle esa autorización por escrito.

  ✓ pedido 12efa2d4-7e71-42ac-bb5e-e58dc77ebfd8


