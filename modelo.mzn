% Modelo base - Concierto de Benito-Bad
% Distancia Manhattan, ubicación en coordenadas enteras,
% el concierto no puede estar dentro de una ciudad.

int: N;                        % tamaño del cuadrado N x N
int: M;                        % número de ciudades
array[1..M] of int: X;         % posición X de cada ciudad
array[1..M] of int: Y;         % posición Y de cada ciudad
array[1..M] of string: nombres;

% Ubicación del concierto
var 0..N: cx;
var 0..N: cy;

% Distancia Manhattan del concierto a cada ciudad
array[1..M] of var 0..2*N: d =
    [abs(cx - X[i]) + abs(cy - Y[i]) | i in 1..M];

% El concierto no puede estar dentro de una ciudad (distancia 0)
constraint forall(i in 1..M)(d[i] >= 1);

% Distancia mínima y máxima a las ciudades
var 0..2*N: dmax = max(d);
var 0..2*N: dmin = min(d);

% Objetivo: primero minimizar la disparidad (dmax - dmin),
% y después la distancia máxima. El factor 2*N hace que
% la disparidad siempre pese más que dmax.
solve minimize 2*N*(dmax - dmin) + dmax;

output ["Concierto en (", show(cx), ", ", show(cy), ")\n",
        "Distancia maxima: ", show(dmax),
        ", minima: ", show(dmin), "\n"]
    ++ [nombres[i] ++ ": " ++ show(d[i]) ++ "\n" | i in 1..M];