# Listas: list

mi_lista = [1, "hola", 3.14]
print(mi_lista)
print(type(mi_lista))

proyectos = [
    "Calculadora",  # 0  -5
    "Agenda de contactos",  # 1  -4
    "Juego de ahorcado",  # 2  -3
    "Lista de compras",  # 3  -2
    "Conversor de monedas",  # 4  -1
]

# Longitud de elementos de una lista
print(len(proyectos))

# Obtener un elemento
print(proyectos[0])
print(proyectos[1])
print("último elemento:")
print("***************")
ultimo_elemento = proyectos[4]
print(ultimo_elemento)
ultimo_elemento = proyectos[-1]
print(ultimo_elemento)
print(type(ultimo_elemento))

# Crear elementos
# proyectos[5] = "Juego de ajedrez"  # error
proyectos.append("Sistema contable")
proyectos += ["Chat con IA"]

nueva_idea = input("¿Cuál es tu proyecto? ")
proyectos.append(nueva_idea)
print(proyectos)

# Cambiar / actualizar
proyectos[0] = "Super calculadora"
print(proyectos)

# Eliminar
del proyectos[0]
print(proyectos)