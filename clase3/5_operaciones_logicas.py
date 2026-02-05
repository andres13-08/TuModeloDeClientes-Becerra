trabaja = True
no_trabaja = False

cliente_1 = no_trabaja
cliente_2 = no_trabaja

print("¿Hoy puede dar un préstamo?")
puedo_dar_prestamo = cliente_1 or cliente_2
print(puedo_dar_prestamo)