from clientes_pkg.cliente import Cliente

# Crear objetos (instancias)
cliente1 = Cliente("Supremo", "supremo@test.com", 5000000, True)

# Probar métodos
print(cliente1)
cliente1.agregar_al_carrito("Apartamento Zona Norte")
cliente1.realizar_compra()