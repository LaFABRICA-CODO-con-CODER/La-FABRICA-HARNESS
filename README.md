# demo-bug

Repositorio de demostración de la fábrica SDD de Emancipación (C3, `codo-fabrica-sdd`).

- Solo biblioteca estándar de Python 3: **sin dependencias de red** (los agentes no tienen salida).
- Bug reproducible: `estadistica.media()` divide entre `len(datos) - 1` y además falla con la lista vacía.
- Test: `python3 -m unittest discover -s tests -v` (hoy falla; debe pasar tras el arreglo).

Las ramas de la fábrica son `sdd/<slug>`; `main` solo cambia por PR revisado por el operador.
