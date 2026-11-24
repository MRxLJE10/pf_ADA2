class ErrorEntrada(Exception):
    pass


def leer_entrada(texto):
    """Devuelve (N, ciudades), donde ciudades es una lista de (nombre, x, y)."""
    lineas = [linea.strip() for linea in texto.splitlines() if linea.strip()]

    if len(lineas) < 2:
        raise ErrorEntrada("Faltan líneas: se requieren N y M.")

    try:
        N = int(lineas[0])
        M = int(lineas[1])
    except ValueError:
        raise ErrorEntrada("N y M deben ser enteros.")

    if N <= 0:
        raise ErrorEntrada("N debe ser mayor que 0.")
    if M <= 0:
        raise ErrorEntrada("M debe ser mayor que 0.")
    if len(lineas) != 2 + M:
        raise ErrorEntrada(
            f"Se esperaban {M} ciudades y llegaron {len(lineas) - 2} líneas."
        )

    ciudades = []
    for linea in lineas[2:]:
        partes = linea.split()
        if len(partes) < 3:
            raise ErrorEntrada(f"Línea incompleta: '{linea}'")

        nombre = " ".join(partes[:-2])
        try:
            x = int(partes[-2])
            y = int(partes[-1])
        except ValueError:
            raise ErrorEntrada(f"Coordenadas no enteras en: '{linea}'")

        if not (0 <= x <= N and 0 <= y <= N):
            raise ErrorEntrada(f"{nombre} está fuera del Valle (0..{N}).")

        ciudades.append((nombre, x, y))

    nombres = [c[0] for c in ciudades]
    if len(set(nombres)) != M:
        raise ErrorEntrada("Hay nombres de ciudad repetidos.")

    posiciones = [(c[1], c[2]) for c in ciudades]
    if len(set(posiciones)) != M:
        raise ErrorEntrada("Dos ciudades están en la misma posición.")

    return N, ciudades


def a_dzn(N, ciudades):
    """Genera el texto de datos (.dzn) que usa modelo.mzn."""
    M = len(ciudades)
    X = [c[1] for c in ciudades]
    Y = [c[2] for c in ciudades]
    nombres = "[" + ", ".join(f'"{c[0]}"' for c in ciudades) + "]"
    return f"N = {N};\nM = {M};\nX = {X};\nY = {Y};\nnombres = {nombres};\n"


if __name__ == "__main__":
    texto_ejemplo = """12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
RioFrio 1 2"""

    N, ciudades = leer_entrada(texto_ejemplo)
    print("Ciudades:", ciudades)
    print("--- Datos para MiniZinc ---")
    print(a_dzn(N, ciudades))