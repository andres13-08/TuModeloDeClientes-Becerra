# Pedir al usuario su edad
#Si es menor a 13, mostrar "Eres un niño"
# Si es menor a 18, mostrar "Eres un adolescente"
# Si es menor a 65, mostrar "Eres un adulto" 
# Si es menor a 75, mostrar "Eres un adulto mayor"
# Si es menor a 120, mostrar "Eres un anciano"
# Si es mayor a 120, mostrar "Edad inválida"

# NO USAR ELIF NI FOR

EDAD = int(input("Ingrese su edad: "))
if EDAD < 13:
    print("Eres un niño")
else:
    if EDAD < 18:
        print("Eres un adolescente")
    else:
        if EDAD < 65:
            print("Eres un adulto")
        else:
            if EDAD < 75:
                print("Eres un adulto mayor")
            else:
                if EDAD < 120:
                    print("Eres un anciano")
                else:
                    print("Edad inválida")