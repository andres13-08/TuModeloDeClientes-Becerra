# Actividad: Crédito Bancario
# Para aplicar a un crédito bancario, el usuario debe ser mayor de edad.
# Además, antiguedad financiera en el sistema de más de 3 años.
# Y un ingreso superior a 2500 dólares mensuales.
# En caso de no tener la antiguedad, su ingreso mensual debe ser superior a 4000 dólares.
# Si no cumple ninguna, no se le da el crédito. 

print("Bienvenido al sistema de crédito bancario")
nombre = input("Por favor ingrese su nombre: ")
edad = int(input("Por favor ingrese su edad: "))

if edad >= 18:
    antiguedad = int(input("Por favor ingrese su antiguedad financiera en años: "))
    if antiguedad >= 3:
        ingreso = float(input("Por favor ingrese su ingreso mensual en dólares: "))
        if ingreso > 2500:
            print(f"Felicidades {nombre}, usted califica para el crédito bancario.")
        else:
            print(f"Lo sentimos {nombre}, no califica para el crédito bancario debido a su ingreso mensual.")
    else:
        antiguedad = int(input("Por favor ingrese su antiguedad financiera en años: "))
        if antiguedad <= 3:
            ingreso = float(input("Por favor ingrese su ingreso mensual en dólares: "))
            if ingreso > 4000:
                print(f"Felicidades {nombre}, usted califica para el crédito bancario.")
            else:
                print(f"Lo sentimos {nombre}, no califica para el crédito bancario debido a su ingreso mensual.")
else:
    print(f"Lo sentimos {nombre}, debe ser mayor de edad para calificar para el crédito bancario.")




# OTRA FORMA DE HACERLO

es_mayor_de_edad = edad >= 18
condicion_1 = es_mayor_de_edad and antiguedad >= 3 and ingreso > 2500
condicion_2 = es_mayor_de_edad and ingreso > 4000

if condicion_1 or condicion_2:
    print(f"Felicidades {nombre}, usted califica para el crédito bancario.")
else:
    print(f"Lo sentimos {nombre}, no califica para el crédito bancario.")