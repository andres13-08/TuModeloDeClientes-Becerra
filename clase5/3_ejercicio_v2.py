# Actividad: Welcome
# Consigna: escribir una funcionalidad a la que se le pase una cadena de nombre de la ciudad, 
# Y muestre por pantalla "Hola, bienvenido a [ciudad]".


def introducir_ciudad() -> str:
    return input("Ciudad: ")

def dar_bienvenida (ciudad:str) -> None:
    print(f"Hola, bienvenido a {ciudad.upper()}")

def principal():
    ciudad = introducir_ciudad()
    bienvenida = dar_bienvenida(ciudad)
    print(bienvenida)

principal()