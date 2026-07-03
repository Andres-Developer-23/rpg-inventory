# Inventario RPG

Sistema de inventario para juegos de rol por terminal, escrito en Python. Permite gestionar objetos organizados por categorías con persistencia en JSON.

## Categorías

- Objetos Comunes
- Poké Balls
- Objetos Clave
- Bayas
- MT/MO

## Uso

```bash
python3 inventario.py
```

Menú interactivo con 3 opciones:

1. **Guardar item** — seleccioná una categoría y agregá un objeto con nombre, cantidad, efecto y descripción.
2. **Mostrar inventario** — seleccioná una categoría para ver todos sus items guardados.
3. **Salir** — cierra el programa.

Los datos se persisten automáticamente en `inventario.json`.

## Datos de ejemplo

El archivo `inventario.json` incluye 14 items precargados para empezar a explorar el inventario sin tener que cargarlos manualmente.

## Tests

```bash
python3 -m unittest test_inventario.py -v
```

Ejecuta 7 tests que cubren carga, guardado, agregado y visualización de items usando `unittest` con mocks de entrada/salida.
