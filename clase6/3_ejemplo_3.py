from banco import CuentaBancaria

try:
    cuenta = CuentaBancaria("Juan Pérez", 1000)
    cuenta.depositar(500)
    cuenta.retirar(200)
    cuenta.mostrar_saldo()
    
    # Intentar retirar más de lo que hay en la cuenta
    cuenta.retirar(2000)
except ValueError as e:
    print("Error:", e)