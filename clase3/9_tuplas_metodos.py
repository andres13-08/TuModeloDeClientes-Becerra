serie_fibonacci = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
print(serie_fibonacci)

# count()
# devuelve el número de veces que un element oaparece
cuenta = serie_fibonacci.count(1)
print(cuenta)

# index()
# devuelve el índice de la primera aparición de un elemento
valor = 13
indice = serie_fibonacci.index(valor)
print(f"El valor {valor} se encuentra en el índice {indice}")
