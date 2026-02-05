"""
Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras.
Realiza los siguientes puntos usando las funciones integradas
ya vistas y el método slice [ : ] Imprime la lista correspondiente luego de cada punto.
Añade a la lista_1 el 456789 y luego el "Hola Mundo"
Luego añade a la lista_2 "Hola y adiós", y luego 5555
Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]
Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]
Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3
"""

lista_1 = [1, 2, 3]
lista_2 = ["a", "b", "c"]

print("Lista 1:", lista_1)
print("Lista 2:", lista_2)

# Añadir elementos a lista_1
lista_1.append(456789)
lista_1.append("Hola Mundo")
print("Lista 1 después de añadir elementos:", lista_1)

# Añadir elementos a lista_2
lista_2.extend(["Hola y adiós", 5555])
print("Lista 2 después de añadir elementos:", lista_2)

# Generar lista_3 sin el último elemento de lista_1
lista_3 = lista_1[:-1]
print("Lista 3 (lista_1 sin el último elemento):", lista_3)

# Generar lista_4 sin el primero y el último elemento de lista_2
lista_4 = lista_2[1:-1]
print("Lista 4 (lista_2 sin el primero y el último elemento):", lista_4)

# Generar lista_5 con los elementos de lista_4 y lista_3
lista_5 = lista_4 + lista_3
print("Lista 5 (combinación de lista_4 y lista_3):", lista_5)