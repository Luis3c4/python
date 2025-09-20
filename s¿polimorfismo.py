class Animal :
    def hablar(self, sonido):
        print(sonido)
class Perro(Animal):
    pass
class Gato(Animal):
    pass
class Vaca(Animal):
    pass

mi_perro = Perro()
mi_gato = Gato()
mi_vaca = Vaca()
mi_perro.hablar("Guau Guau")
mi_gato.hablar("Miau Miau")
mi_vaca.hablar("Muu Muu")