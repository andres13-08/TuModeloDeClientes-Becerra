while True:
    print("Hola")
    respuesta = input("¿Deseas salir? (s/n): ")
    if respuesta.lower().startswith('s'):
        print("Saliendo del bucle...")
        break
        print("Este mensaje nunca se mostrará si se elige salir")
    elif respuesta.lower().startswith('n'):
        print("Continuando el bucle...")
        continue
        print("Este mensaje nunca se mostrará si se elige continuar")
    else:
        print("Respuesta no válida, por favor ingresa 's' o 'n'")