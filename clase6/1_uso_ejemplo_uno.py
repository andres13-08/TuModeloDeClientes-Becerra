from poo import Libro

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 0)
libro2 = Libro("1984", "George Orwell", 2)
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1)

libro1.estado()

libro1.prestar()
print(libro1.copias)
libro1.devolver()
print(libro1.copias)

prestamo = input("Ingrese el número de libro a prestar: ")
if prestamo == "1":
    libro1.prestar()
elif prestamo == "2":
    libro2.prestar()
elif prestamo == "3":
    libro3.prestar() 

input_devolucion = input("¿Desea devolver un libro? (s/n): ")
if input_devolucion.lower() == "s":
    devolucion = input("Ingrese el número de libro a devolver: ")
    if devolucion == "1":
        libro1.devolver()
    elif devolucion == "2":
        libro2.devolver()
    elif devolucion == "3":
        libro3.devolver()
elif input_devolucion.lower() == "n":
    print("Devuelvame el libro cuando pueda.")