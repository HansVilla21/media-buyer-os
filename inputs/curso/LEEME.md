# El curso

Media Buyers HQ, de Sebastián Gómez (mediabuyers.ai). Hans lo descargó en
`C:\Users\hvill\Downloads\Media Buyer HQ\`: una carpeta por sesión con el video `.mp4` y sus
recursos, más `Recursos\` con el FAQ y el Protocolo Ad Budget. **Los videos viven ahí, no acá:**
pesan 3 GB. Si Hans los mueve, se actualizan esta nota y los `fuente.md`.

Sesiones disponibles al 2026-10-09: 2–9, 17 y 18. La 1 fue la introducción al programa y no se
procesa. La carpeta «Sesion 17» trae el video `sesion-10-media-buyer-delivery.mp4`; se toma como
la sesión 17.

Acá queda, por sesión, la materia prima en texto:

```
inputs/curso/
├── recursos/                 recursos que se repiten entre sesiones: una sola copia, original + texto
└── sesion-NN-tema/
    ├── fuente.md             ruta del video, duración, y cada recurso con de dónde salió
    ├── transcripcion.md      transcripción completa, por párrafos con minuto
    ├── transcripcion.json    cada segmento con tiempos y confianza (la forma sin pérdida)
    └── recursos/             cada recurso original y su versión en texto (.pdf.md, .xlsx.md)
```

Cómo se produce: `scripts/transcribe.py` (video → transcripción, en esta máquina, con la GPU) y
`scripts/convert_resources.py` (recursos → texto; detecta los repetidos por hash).

Nada de acá se edita a mano. Lo que el media buyer aprende va a `knowledge/`.
