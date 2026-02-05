# Crear un bucle while que piuda al usuario un número. Si el número es menor a 1, salir del blucle.
# --> Crear un bloque else que imprima "fin del programa"

proceder = True # bandera o flag.

while proceder:     
    numero = int(input("Ingrese un número: "))
    if numero < 1:
        proceder = False
else:
    print("Fin del programa")