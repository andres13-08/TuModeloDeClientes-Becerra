# Consigna
# Para tu primera entrega, te proponemos que crees un programa que permita emular el registro 
# y almacenamiento de usuarios en una base de datos. Hazlo utilizando el concepto de funciones, 
# diccionarios, bucles y condicionales.

# Objetivos
# 1. Practicar el concepto de funciones.
# 2. Desarrollar la parte lógica para el registro de usuarios.

# Requisitos
# Diccionarios (guardado de datos)
# Input (solicitud de datos)
# Variables
# If (chequeo de datos)
# While (iteración para el programa, sea para agregar, loguear o mostrar)
# For (recorrer datos y para búsqueda)
# Print
# Funciones separadas para registro, almacenamiento y muestra

# Recomendaciones
# 1. El formato de registro es: Nombre de usuario y Contraseña.
# 2. Utilizar una función para almacenar la información y otra función para mostrar
#    la información.
# 3. Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña 
#    (clave-valor).
# 4. Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida 
#    con el usuario.

base_de_datos = {
    "andres": "clave1234",
    "maria": "maria5678",
    "juan": "juan91011"
}

def mostrar_usuarios():
    for usuario, clave in base_de_datos.items():
        print(f"Usuario: {usuario}, Clave: {clave}")

def registrar_usuario():
    nuevo_usuario = input("Cree su nombre de usuario: ")
    nueva_clave = input("Cree su clave: ")
    
    if 3 <= len(nuevo_usuario) <= 10:
        base_de_datos[nuevo_usuario] = nueva_clave
        print("¡Usuario registrado con éxito!")
    else:
        print("Error: El usuario debe tener entre 3 y 10 caracteres.")

def login():
    intentos = 0
    while intentos < 3:
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su clave: ")
        
        if user in base_de_datos and base_de_datos[user] == password:
            print(f"¡Bienvenido {user}! Acceso concedido.")
            return True
        else:
            intentos += 1
            print(f"Acceso denegado. Intento {intentos} de 3.")
    return False

while True:
    print("1. Registrar Usuario\n2. Hacer Login\n3. Mostrar Base de Datos\n4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        if login(): 
            break # Sale si el login es exitoso
    elif opcion == "3":
        mostrar_usuarios()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")