"""
A partir del siguiente diccionario, realizar los ejercicios propuestos:

inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}

# Agregar 5 manzanas más al inventario
# Se vendieron 3 naranjas, actualizar el inventario
# Se agregaron 5 uvas"
"""

inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8,
}
print(inventario)

# Agregar 5 manzanas más al inventario
inventario["manzanas"] += 5

# Se vendieron 3 naranjas, actualizar el inventario
inventario["naranjas"] -= 3

# Se agregaron 5 uvas"
inventario["uvas"] = 5


print(inventario)