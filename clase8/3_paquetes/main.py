import matematicas.calculo_areas
import matematicas.operaciones

resultado_suma = matematicas.operaciones.sumar(5, 3)
resultado_resta = matematicas.operaciones.restar(10, 4)
resultado_area_rectangulo = matematicas.calculo_areas.area_rectangulo(4, 2)
resultado_area_circulo = matematicas.calculo_areas.area_circulo(3)

print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Área del rectángulo: {resultado_area_rectangulo}")
print(f"Área del círculo: {resultado_area_circulo}")