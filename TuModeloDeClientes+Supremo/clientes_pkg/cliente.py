class Cliente:
    # Atributo de clase
    empresa = "Nexus Inmobiliaria"

    def __init__(self, nombre, email, presupuesto, es_inversionista):
        # Atributos de instancia (Mínimo 4)
        self.nombre = nombre
        self.email = email
        self.presupuesto = presupuesto
        self.es_inversionista = es_inversionista
        self.intereses = []

    # Método mágico __str__ (Para darle nombre al objeto al imprimirlo)
    def __str__(self):
        return f"Cliente Registrado: {self.nombre} ({self.email})"

    # Método propio 1: Agregar interés
    def agregar_interes(self, proyecto):
        self.intereses.append(proyecto)
        print(f"🏠 {self.nombre} ha mostrado interés en: {proyecto}")

    # Método propio 2: Aplicar descuento (Lógica de negocio)
    def verificar_perfil(self):
        if self.es_inversionista:
            print(f"💎 {self.nombre} es cliente VIP. Aplicar tasa preferencial.")
        else:
            print(f"👤 {self.nombre} es cliente estándar.")

# Crear el objeto
cliente_test = Cliente("Andrés Becerra", "andres@mail.com", 450000000, True)

# Probarlo
print(cliente_test)
cliente_test.agregar_interes("Apartamento La Felicidad")
cliente_test.verificar_perfil()