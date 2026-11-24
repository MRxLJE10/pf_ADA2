# Modelo del problema

## Conjuntos y parámetros
- N: tamaño del Valle de Cauca (cuadrado de N x N km), con N > 0.
- M: número de ciudades, con M > 0.
- (x_i, y_i): posición entera de la ciudad i, con 0 <= x_i, y_i <= N, para i = 1..M.
- Todas las ciudades tienen posiciones distintas.

## Variables de decisión
- (cx, cy): posición del concierto, con 0 <= cx, cy <= N, donde cx y cy son enteros.

## Distancia
La distancia entre el concierto y la ciudad i es la distancia Manhattan:

d_i = |cx − x_i| + |cy − y_i|

## Restricciones
- El concierto no puede estar dentro de una ciudad: d_i >= 1 para todo i.

## Medidas auxiliares
- d_max = max(d_1, ..., d_M): distancia a la ciudad más lejana.
- d_min = min(d_1, ..., d_M): distancia a la ciudad más cercana.
- Disparidad = d_max − d_min: diferencia entre la ciudad más lejana y la más cercana. Es la medida de "favorecer" a una ciudad.

## Función objetivo
Minimizar:

f = 2N · (d_max − d_min) + d_max

Criterio de equidad: el objetivo principal es reducir la disparidad, porque es lo que hace que una ciudad quede favorecida frente a otra. El objetivo secundario es reducir la distancia máxima, para que el concierto quede lo más cerca posible de todas las ciudades.

## Justificación de los pesos
d_max toma valores entre 1 y 2N, así que su variación en el objetivo nunca supera 2N − 1. Por eso el peso 2N de la disparidad garantiza que una unidad menos de disparidad siempre vale más que cualquier cambio en d_max. El objetivo se comporta como una optimización lexicográfica: primero equidad, luego cercanía.

## Justificación de supuestos
- Posición entera del concierto: las ciudades están en intersecciones enteras y el enunciado pide ubicar el concierto en el plano del Valle. Asumimos que el concierto también debe ubicarse en una intersección. Esto es un supuesto de modelado. Una posición real (no entera) podría dar un óptimo distinto, y lo señalamos como limitación.
- Distancia Manhattan: es la medida que indica la gobernación en el enunciado.
- Restricción d_i >= 1: el concierto no puede coincidir con una ciudad, porque eso generaría un "duelo" entre alcaldes.

## Limitaciones y casos especiales
- Pueden existir varias soluciones con el mismo valor óptimo. El modelo devuelve solo una, sin criterio de desempate explícito.
- Si la ciudad más lejana y la más cercana están a la misma distancia, la disparidad es 0 y el modelo busca la mínima distancia máxima.
- El criterio de equidad es una decisión de modelado. Otros criterios posibles son minimizar la suma de distancias o la distancia máxima sola. Se comparan en el análisis de pruebas.