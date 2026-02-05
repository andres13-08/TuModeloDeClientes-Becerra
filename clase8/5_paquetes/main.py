# from matematicas.calculo_areas import area_circulo, area_rectangulo
# from matematicas.operaciones import restar, sumar
import matematicas


def main():
    resultado_suma = matematicas.sumar(5, 3)
    resultado_resta = matematicas.restar(10, 4)
    resultado_area_rectangulo = matematicas.area_rectangulo(4, 2)
    resultado_area_circulo = matematicas.area_circulo(3)

    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    print(f"Área del rectángulo: {resultado_area_rectangulo}")
    print(f"Área del círculo: {resultado_area_circulo}")


main()