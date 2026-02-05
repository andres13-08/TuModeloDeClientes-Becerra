"""Consigna: Crear una variable que almacene si se cumplen todas las condiciones.
A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable que almacene si se cumplen todas las siguientes condiciones, 
encadenando operadores lógicos en una sola línea:

NOMBRE sea diferente de cuatro asteriscos “”
EDAD sea mayor que 5 y a su vez menor que 20
Que la longitud de NOMBRE sea mayor o igual a 4 pero a la vez menor que 8
EDAD multiplicada por 3 sea mayor que 35
Desde un input conseguir las variables:
nombre = INPUT!!!
edad = INPUT!!!!

Duración: 10 minutos
"""
# DATOS
NOMBRE = input("Ingrese su nombre: ")
EDAD = int(input("Ingrese su edad: "))

# OPERACIONES
expresion_1 = NOMBRE != "****"
expresion_2 = EDAD > 5 and EDAD < 20
expresion_3 = len(NOMBRE) >= 4 and len(NOMBRE) < 8
expresion_4 = EDAD * 3 > 35
cumplen_todas_las_condiciones = expresion_1 and expresion_2 and expresion_3 and expresion_4

# RESPUESTA EN CONSOLA
print("Nombre no es de ****", expresion_1)
print("Edad es mayor a 5 y menor a 20:", expresion_2)
print("Longitud de nombre es mayor o igual a 4 y menor a 8:", expresion_3)
print("Edad multiplicada por 3 es mayor a 35:", expresion_4)
print("Cumple todas las condiciones:", cumplen_todas_las_condiciones)