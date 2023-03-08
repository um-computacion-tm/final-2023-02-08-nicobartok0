class Dispositivo:
    def __init__(self, id, nombre, marca=None, tipo=None):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.tipo = tipo 

    def __repr__(self):
        if self.tipo != None and self.marca != None:
            return f'{self.id, self.nombre, self.marca, self.tipo}'
        elif self.tipo != None and self.marca == None:
            return f'{self.id, self.nombre, self.tipo}'
        elif self.tipo == None and self.marca != None:
            return f'{self.id, self.nombre, self.marca}'