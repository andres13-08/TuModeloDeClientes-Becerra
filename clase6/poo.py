# Queremos representar un libro de una biblioteca. Cada librot tiene un título, un autor y un
# números de copias disponibles. Podrá prestarlo y devolverlo.

class Libro:
    def __init__(self, titulo, autor, copias):
        if copias < 0:
            raise ValueError("El número de copias no puede ser negativo")   
        
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def prestar(self):
        if self.copias == 0:
            print("No hay copias disponibles para prestar.")
        else:
            self.copias -= 1
            print(f"Has prestado una copia de '{self.titulo}'.")
    
    def devolver(self):
        self.copias += 1
    
    def estado(self):
        print(f"Título: {self.titulo} del Autor: {self.autor}, tiene {self.copias} Copias disponibles")