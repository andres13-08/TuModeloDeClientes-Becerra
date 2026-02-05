class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        if not titular:
            raise ValueError("El titular no puede estar vacío.")
        
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo.")
        
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        
        self.saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes para realizar el retiro.")
        
        self.saldo -= monto

    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es: ${self.saldo}")