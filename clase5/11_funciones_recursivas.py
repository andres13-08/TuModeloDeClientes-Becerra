def sumar(a, b):
    print(a + b)
    return

def restar(a, b):   
    print(a - b)
    return

def menu():
    while True:
        print("Seleccione la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Salir")
        eleccion = input("Ingrese 1 - 2 - 3: ")

        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if eleccion == "1":
            sumar(num1, num2)
            print("Operación de suma realizada: {sumar}")
        elif eleccion == "2":
            restar(num1, num2)
        elif eleccion == "3":
            break
        else:
            continue

menu()