# Media Buyer OS

El media buyer de Hans: consigue conversaciones con dueños de negocio que encajan, pagando anuncios en
Meta. Se entrenó con el curso Media Buyers HQ (Sebastián Gómez), sesión a sesión, y trabajó un primer caso
real: la oferta y la primera campaña de Hans (2026-10-07 a 2026-10-23).

> **Privado.** Trae material pagado del curso, el texto de libros de Hormozi y datos de clientes: no se
> hace público ni se comparte con terceros.

**Para replicarlo:** abrir Claude Code en una carpeta vacía y pegarle esto:

```text
Cloná acá el repositorio privado HansVilla21/media-buyer-os (gh repo clone HansVilla21/media-buyer-os .) y replicá el media buyer siguiendo REPLICAR.md.
```

**Para trabajar en el original:** Claude Code en la carpeta. Todo lo que hace falta saber está en
`CLAUDE.md`. Para pasarle el curso: cada sesión nueva en `inputs/curso/`.

## Qué hay

| Dónde | Qué tiene |
|---|---|
| `CLAUDE.md` | el método, las reglas y cómo trabajar con Hans |
| `.claude/skills/` | 20 skills del oficio, cada una con su estado |
| `inputs/curso/` | las 10 sesiones (2–9, 17 y 18; 16 h 44 min de video): transcripción con minutos y recursos |
| `knowledge/curso/` | apuntes y examen por sesión, con su `indice.md` |
| `knowledge/manual/` | 15 notas por tema: lo que se consulta para trabajar |
| `knowledge/referencias/` · `inputs/referencias/` | Hormozi, competencia y políticas de Meta |
| `memory/` | la bitácora: estado, tareas, decisiones, aprendizajes y handoffs |
| `output/` | todo lo producido: oferta, diagnósticos, copies, campañas y clientes |
| `scripts/` | el transcriptor local y el conversor de recursos, con `requirements.txt` |
| `REPLICAR.md` · `replicar/` | cómo levantar una copia, y la memoria automática del original |

No están los videos del curso ni el entorno y los modelos del transcriptor (`.venv/`, `.cache/`): ver
`REPLICAR.md`.
