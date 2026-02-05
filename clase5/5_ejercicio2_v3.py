# Actividad: Media
# Consigna: escribir una funcionalidad que reciba una muestra de números de una lista y devuelva la media aritmética
# de dichos números.


def promediar(lista_de_notas):
    promedio = sum(lista_de_notas) / len(lista_de_notas)
    return promedio

def principal():
    lista_de_notas = [34, 12, 976, 34, 123]
    promedio = promediar(lista_de_notas)
    print(promedio)

principal()