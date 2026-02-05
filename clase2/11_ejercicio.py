# Actividad: Desafío de Tuplas
# Consigna:
# A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada,
# lo siguiente:

# El último ítem de tupla
# El número de ítems de tupla
# La posición donde se encuentra el ítem 87 de tupla
# Una lista con los últimos tres ítems de tupla
# Un ítem que haya en la posición 8 de tupla
# El número de veces que el ítem 7 aparece en tupla

# Copia esta tupla para iniciar el ejercicio:
# tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

# El último ítem de tupla
print(tupla[-1])

# El número de ítems de tupla
print(len(tupla))

# La posición donde se encuentra el ítem 87 de tupla
print(tupla.index(87))

# Una lista con los últimos tres ítems de tupla
print(list(tupla[-3:]))

# Un ítem que haya en la posición 8 de tupla
print(tupla[7])

# El número de veces que el ítem 7 aparece en tupla
print(tupla.count(7))