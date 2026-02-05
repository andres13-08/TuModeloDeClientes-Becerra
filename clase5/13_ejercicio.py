credenciales = [
    {"usuario": "andres", "clave": "1234"},
    {"usuario": "maria", "clave": "abcd"},
    {"usuario": "juan", "clave": "xyz987"},
]

input_usuario = input("Ingrese su usuario: ")
input_clave = input("Ingrese su clave: ")   

for credencial in credenciales:
    if credencial["usuario"] == input_usuario and credencial["clave"] == input_clave:
        print("Acceso concedido")
        break
    else:
        print("Acceso denegado")
        break