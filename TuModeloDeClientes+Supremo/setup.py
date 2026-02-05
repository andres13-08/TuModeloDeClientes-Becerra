"""
Consigna:
Crea un programa que permita el modelamiento de Clientes en una página de compras.
Se debe utilizar Programación Orientada a Objetos.

Se evaluará el uso correcto de atributos y métodos.
Crea un paquete redistribuible con el programa creado.

Objetivos
Demostrar la comprensión de los conceptos de “Clases” y “Objetos”

Ejecutar correctamente el uso de paquetes y librerías.

Requisitos:
- Clases (para cliente)
- Atributos de instancia (opcional alguno de clase)
- Métodos (por fuera de los magic methods)
- Uso de módulos/paquetes
- Generación de paquete redistribuible

Recomendaciones:
- La Clase Cliente debe tener mínimo 4 atributos
- Se debe utilizar el método __init__ para definir uno o más de los atributos
- Se debe utilizar el método __str__() para darle nombre a los objetos
- Aparte, genera 2 métodos por fuera de los magic methods
- Para crear el paquete distribuible incluir también el archivo de la Pre entrega #1

Formato:
- El proyecto debe ser un archivo comprimido del paquete
- Formatos aceptados: .zip o .tar.gz bajo el nombre "TuModeloDeClientes+Apellido"
- Ejemplo: "TuModeloDeClientes+Fernandez"

Contenidos adicionales (optativos):
- Uso de herencia
- Uso de archivos
"""

# Inicia tu código aquí

from setuptools import setup

setup(
    name="TuModeloDeClientes_Supremo",
    version="1.0",
    description="Paquete para modelamiento de clientes - Pre-entrega 2",
    author="Supremo",
    packages=["clientes_pkg"],
)
