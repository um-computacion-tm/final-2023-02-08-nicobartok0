from dispositivo import Dispositivo

class Database:
    def __init__(self, template):
        self.elements = template['dispositivos']
        self.database = []
        for element in self.elements:
            id = element['id']
            nombre = element['nombre']
            marca = element.get('marca')
            tipo = element.get('tipo')

            dispositivo = Dispositivo(id, nombre, marca, tipo)
            self.database.append(dispositivo)
        print(self.database)

    def delete_by_id(self, id):
        current = -1
        for element in self.database:
            current +=1
            if id == element.id:
                del self.database[current]


    def add_dispositivo(self, dispositivo:Dispositivo):
        self.database.append(dispositivo) 
