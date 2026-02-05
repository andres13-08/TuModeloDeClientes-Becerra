from colegio.alumnos import Alumno


def main():
    juan = Alumno(nombre="Juan", nota=7)
    rodrigo = Alumno(nombre="Rodrigo", nota=8)
    juan.mostrar_nota()
    rodrigo.mostrar_nota()


if __name__ == "__main__":
    main()