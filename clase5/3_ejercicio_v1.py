# Actividad: Welcome
# Consigna: escribir una funcionalidad a la que se le pase una cadena de nombre de la ciudad, 
# Y muestre por pantalla "Hola, bienvenido a [ciudad]".


def introducir_ciudad():
    ciudad = input("Ciudad: ")
    return ciudad

def dar_bienvenida (ciudad):
    print(f"Hola, bienvenido a {ciudad}")

def principal():
    ciudad = introducir_ciudad()
    dar_bienvenida(ciudad)

principal()