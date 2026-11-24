# Concierto de Benito-Bad: ubicación óptima con MiniZinc

Proyecto 2 de Análisis y Diseño de Algoritmos (Universidad del Valle, 2026-2).

Ubica el concierto del cantante Benito-Bad en el Valle del Cauca, modelado como un cuadrado de N x N km. La distancia entre dos puntos es la distancia Manhattan. El concierto debe quedar en una posición entera, no puede coincidir con una ciudad y debe ser lo más equitativo posible para todas las ciudades.

## Contenido del proyecto

| Archivo | Descripción |
|---|---|
| `entrada.py` | Lee la entrada del problema, valida los datos y genera el bloque de datos para MiniZinc. |
| `modelo.mzn` | Modelo en MiniZinc: variables, restricciones y función objetivo. |
| `ejemplo.dzn` | Caso de prueba con N = 10 y 4 ciudades (el ejemplo del enunciado). |
| `modelo_formal.md` | Descripción matemática del problema, usada en el informe. |

## Formato de entrada

La entrada es texto con esta estructura:

```
N
M
nombre_ciudad X Y
...
```

- `N`: tamaño del cuadrado del Valle (entero positivo).
- `M`: número de ciudades (entero positivo).
- Cada una de las M líneas siguientes contiene el nombre de la ciudad, su posición X y su posición Y, separados por espacios.

Ejemplo:

```
12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
RioFrio 1 2
```

El nombre de la ciudad no puede tener saltos de línea. Si tiene espacios, deben ir todos antes de las dos coordenadas.

## Requisitos

- Python 3.8 o superior, para `entrada.py`.
- MiniZinc, para ejecutar `modelo.mzn`. Puede usarse el MiniZinc IDE o la línea de comandos.

## Cómo ejecutar

### 1. Validar la entrada y generar los datos

```bash
python entrada.py
```

Imprime las ciudades leídas y el bloque de datos en formato `.dzn`. La función `leer_entrada` lanza un error si la entrada no cumple el formato, por ejemplo cuando faltan ciudades, hay coordenadas fuera del Valle o hay posiciones repetidas.

### 2. Resolver con MiniZinc

Con el MiniZinc IDE: abre `modelo.mzn`, selecciona `ejemplo.dzn` como archivo de datos y presiona Run.

Con la línea de comandos:

```bash
minizinc modelo.mzn ejemplo.dzn
```

### Resultado esperado para `ejemplo.dzn`

```
Concierto en (2, 6)
Distancia maxima: 4, minima: 1
La Union: 4
Cali: 4
Tulua: 1
San Pedro: 3
----------
==========
```

## Modelo

Las decisiones del modelo son:

- La posición del concierto `(cx, cy)` es entera y está dentro del Valle.
- La distancia a cada ciudad es `d_i = |cx − x_i| + |cy − y_i|`.
- El concierto no puede estar en una ciudad (`d_i >= 1`).
- El objetivo es minimizar `2N · (d_max − d_min) + d_max`. Primero reduce la disparidad entre la ciudad más lejana y la más cercana (equidad) y luego la distancia máxima (cercanía).

El detalle matemático y la justificación de los supuestos están en `modelo_formal.md`.

## Limitaciones conocidas

- Si hay varias ubicaciones óptimas, el modelo devuelve solo una.
- El concierto se limita a posiciones enteras, siguiendo la forma en que se describen las ciudades.
- El criterio de equidad es una decisión de modelado y puede cambiarse en `modelo.mzn`.

## Autores

- Juan Sebastian Pérez 2459371
- Victor Murillo 2459569
- Mariana Rios 2459759