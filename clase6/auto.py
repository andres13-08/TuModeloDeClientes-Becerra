class Auto:

    def __init__(self, marca, color, precio, patente, puertas):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.patente = patente
        self.puertas = puertas

    def arrancar(self):
        print(f"El auto {self.marca} con patente {self.patente} ha arrancado.")