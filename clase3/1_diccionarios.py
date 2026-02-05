# Diccionarios <dict>
# Colección mutable, de índices desordenados, no indexada, con claves únicas,
# guardan pares clave-valor

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "nacionalidades": ["española", "argentina"],
}
print(type(diccionario))
print(diccionario)
print(len(diccionario))

# Obtener datos
print(diccionario["nombre"])
print(diccionario.get("nombre"))

nacionalidad_española = diccionario["nacionalidades"][0]
print(nacionalidad_española)

print("española" in diccionario["nacionalidades"])

# Modificar
diccionario["edad"] = 31
diccionario["edad"] = diccionario["edad"] + 1
diccionario["edad"] += 1
print(diccionario)

# Crear
diccionario["altura"] = 1.80
print(diccionario)