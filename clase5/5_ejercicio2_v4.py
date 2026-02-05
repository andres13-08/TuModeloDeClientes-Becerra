# Actividad: Media
# Consigna: escribir una funcionalidad que reciba una muestra de números de una lista y devuelva la media aritmética
# de dichos números.


def promediar(lista_de_notas: list) -> float:
    """Promedia una lista de números."""
    promedio = sum(lista_de_notas) / len(lista_de_notas)
    return promedio

def ver_promedio(promedio: float) -> None:
    """Muestra el promedio por pantalla."""
    print("----- Resultado -----")
    print(f"El promedio es: {promedio}")
    print("---------------------")


def main():
    lista_de_notas = [34, 12, 976, 34, 123]
    promedio = promediar(lista_de_notas)
    ver_promedio(promedio)

main()