class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} de {self.autor} con {self.paginas} páginas"
    
mi_libro = Libro("El principito", "Antoine de Saint-Exupéry", 96)