def sumar(sumando_a: float, sumando_b: float) -> float:
    return sumando_a + sumando_b

def restar(minuendo: float, sustraendo: float) -> float:
    return minuendo - sustraendo

def multiplicar(factor_a: float, factor_b: float) -> float:
    return factor_a * factor_b

def dividir(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    return dividendo / divisor