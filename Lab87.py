# Lab87.py


class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape
        
    def imprimir_nombre(self):
        print(self.nombre, self.apellido)

# Estudiante hereda de Persona, no agrega atributos nuevos por ahora
class Estudiante(Persona):
    pass

x = Estudiante("Mengano", "De Tal")
x.imprimir_nombre()