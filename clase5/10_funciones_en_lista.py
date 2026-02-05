def hola() -> str:
    return "Hola, bienvenido"

def adios() -> str:
    return "Adiós, hasta luego"

saludos = [hola, hola, adios]

for saludar in saludos:
    print(f"Invocando a la función: {saludar()}")