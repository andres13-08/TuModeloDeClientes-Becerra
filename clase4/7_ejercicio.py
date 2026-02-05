# USAR ELIF PARA TENER UN TEXTO MÁS CLARO Y QUITAR LAS INDESACIONES


EDAD = int(input("Ingrese su edad: "))
if EDAD >= 5 and EDAD < 13:
    print("Eres un niño")

elif EDAD >= 14 and EDAD < 18:
    print("Eres un adolescente")

elif EDAD >= 18 and EDAD < 64:
    print("Eres un adulto")

elif EDAD >= 65 and EDAD < 74:
    print("Eres un adulto mayor")

elif EDAD >= 75 and EDAD < 119:
    print("Eres un adulto ya bien mayor")

elif EDAD >= 120 and EDAD < 150:
    print("Eres un anciano")

else:
    print("Edad inválida")