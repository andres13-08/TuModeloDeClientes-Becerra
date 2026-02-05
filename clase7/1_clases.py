class TarjetaCredito:
    def __init__(objeto) -> None:
        objeto.identificacion = None
        objeto.titular = None
        objeto.fecha_vencimiento = None
        objeto.cvc = None

tarjeta_de_juan = TarjetaCredito()
tarjeta_de_juan.titular = "Juan Perez"
tarjeta_de_juan.identificacion = "1234 5678 9012 3456"
tarjeta_de_juan.fecha_vencimiento = "12/25"
tarjeta_de_juan.cvc = "123"

print(tarjeta_de_juan.titular)
print(tarjeta_de_juan.identificacion)
print(tarjeta_de_juan.fecha_vencimiento)
print(tarjeta_de_juan.cvc)