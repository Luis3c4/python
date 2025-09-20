def decorador(func):
    def wrapper():
        print("Antes de llamar a la función")
        func()
        print("Después de llamar a la función")
    return wrapper
@decorador
def saludar():
    print("¡Hola, mundo!")

saludar()

class DecoradorClase:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print("Antes")
        self.func()
        print("Después")
@DecoradorClase
def otra_funcion():
    print("Dentro de otra función")

otra_funcion()