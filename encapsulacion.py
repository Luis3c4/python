class Persona: 
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo privado
        self._edad = edad      # Atributo privado

    # Método getter para nombre
    def get_nombre(self):
        return self._nombre

    # Método setter para nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    # Método getter para edad
    def get_edad(self):
        return self._edad

    # Método setter para edad
    def set_edad(self, edad):
        if edad >= 0:  # Validación simple
            self._edad = edad
        else:
            print("La edad no puede ser negativa.")

mi_persona = Persona("Juan", 30)
mi_persona.set_edad(-1)