class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def obtener_informacion(self):
        return f"'{self.titulo}' por {self.autor}, publicado en {self.anio_publicacion}"

libro1= Libro("1984", "George Orwell", 1949)
print(libro1.obtener_informacion())