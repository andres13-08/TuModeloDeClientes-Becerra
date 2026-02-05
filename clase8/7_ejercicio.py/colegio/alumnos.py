class Alumno:
    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self.nota = nota

    def mostrar_nota(self):
        print(f"Mi nombre {self.nombre} y mi nota: {self.nota}")