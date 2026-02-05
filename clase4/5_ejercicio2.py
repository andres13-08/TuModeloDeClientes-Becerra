# Pedir al usuario su edad
#Si es menor a 13, mostrar "Eres un niño"
# Si es menor a 18, mostrar "Eres un adolescente"
# Si es menor a 65, mostrar "Eres un adulto" 
# Si es menor a 75, mostrar "Eres un adulto mayor"
# Si es menor a 120, mostrar "Eres un anciano"
# Si es mayor a 120, mostrar "Edad inválida"

# NO USAR ELIF NI FOR

EDAD = int(input("Ingrese su edad: "))
if EDAD >= 5 and EDAD < 13:
    print("Eres un niño")

if EDAD < 14 and EDAD < 18:
    print("Eres un adolescente")

if EDAD < 18 and EDAD < 64:
    print("Eres un adulto")

if EDAD < 65 and EDAD < 74:
    print("Eres un adulto mayor")

if EDAD < 75 and EDAD < 119:
    print("Eres un adulto ya bien mayor")

if EDAD < 120 and EDAD < 150:
    print("Eres un anciano")

else:
    print("Edad inválida")
