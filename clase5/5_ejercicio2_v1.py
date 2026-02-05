# Actividad: Media
# Consigna: escribir una funcionalidad que reciba una muestra de números de una lista y devuelva la media aritmética
# de dichos números.


def media_aritmetica (numeros: list) -> float:
    return sum(numeros) / len(numeros)

def principal():
    muestra_numeros = [10, 20, 30, 40, 50]
    resultado = media_aritmetica(muestra_numeros)
    print(f"La media aritmética de {muestra_numeros} es {resultado}")

principal()