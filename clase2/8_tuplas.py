# Tuplas: Son estructuras de datos similares a las listas, pero inmutables.
# Se definen utilizando paréntesis () y pueden contener elementos de diferentes tipos de datos.
# <tuple>

tupla = (1, "hola", 3.4, -12, 0.4)
print(tupla)
print(type(tupla))

# Acceso a elementos de la tupla mediante índices
print(tupla[2])

mi_lista = list(tupla)
print(mi_lista)
mi_lista.append(7)

tupla = tuple(mi_lista)
print(tupla)