temperatura = int(input("Escriba la temperatura: "))

if temperatura > 20:
    print(f"La temperatura es de {temperatura}°C, así que hace calor")

elif temperatura >= 0 and temperatura < 20:
    print(f"La temperatura es de {temperatura}°C, así que está agradable")

elif temperatura < 0 and temperatura >= -10:
    print(f"La temperatura es de {temperatura}°C, así que hace frío")

else:
    print(f"La temperatura es de {temperatura}°C, así que no sé qué decirte")