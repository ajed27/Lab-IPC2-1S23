class Elemento():
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return "id: " + self.id + " nombre: " + self.nombre
