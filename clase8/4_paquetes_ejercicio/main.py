from matematicas.calculo_areas import area_circulo, area_rectangulo, pi
from matematicas.operaciones import restar, sumar

resultado_suma = sumar(5, 3)
resultado_resta = restar(10, 4)
resultado_area_rectangulo = area_rectangulo(4, 2)
resultado_area_circulo = area_circulo(3)

print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Área del rectángulo: {resultado_area_rectangulo}")
print(f"Área del círculo: {resultado_area_circulo}")