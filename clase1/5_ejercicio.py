"""
Descripción de la actividad.
En nuestro trabajo, nos solicitan desarrollar un programa
que permita calcular el promedio final de los equipos de fútbol en un torneo.
Para ello, debemos considerar tres aspectos:
Jugaron 20 partidos durante el torneo.
Los partidos poseen diferente puntaje según el resultado:
los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos.
El promedio final resulta de la cantidad de puntos totales divididos
la cantidad de partidos.
"""

# Declaración datos
PUNTOS_GANADO = 3
PUNTOS_EMPATADO = 1
PUNTOS_PERDIDO = 0
PARTIDOS_JUGADOS = 20

# Entrada
partidos_ganados = int(input("¿Cuántos partidos ganó el equipo? "))
partidos_empatados = int(input("¿Cuántos partidos empató el equipo? "))
partidos_perdidos = int(input("¿Cuántos partidos perdió el equipo? "))

# Operaciones
puntos_totales = (
    partidos_ganados * PUNTOS_GANADO
    + partidos_empatados * PUNTOS_EMPATADO
    + partidos_perdidos * PUNTOS_PERDIDO
)
promedio = puntos_totales / PARTIDOS_JUGADOS

# Salida
print(f"El promedio final de puntos: {promedio}")