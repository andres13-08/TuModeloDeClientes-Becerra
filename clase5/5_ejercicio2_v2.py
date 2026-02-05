# Actividad: Media
# Consigna: escribir una funcionalidad que reciba una muestra de números de una lista y devuelva la media aritmética
# de dichos números.


def promediar():
    promedio = sum(lista_de_notas) / len(lista_de_notas)
    return promedio

lista_de_notas = [7, 8, 9, 6, 985]

promedio = promediar()
print(promedio)