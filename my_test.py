import unittest

from dispositivo import Dispositivo
from database import Database


class MyTest(unittest.TestCase):

    def setUp(self):
        self.database_template = {"dispositivos": [
            {
                "id": 1,
                "nombre": "teclado",
                "marca": "genius",
            },
            {
                "id": 2,
                "nombre": "mouse",
                "marca": "logitech",
            },
            {
                "id": 3,
                "nombre": "memoria",
                "tipo": "ram",
            }
        ]}

        self.dispositivo1 = Dispositivo(1, "teclado", "genius")
        self.dispositivo2 = Dispositivo(2, "mouse", "logitech")
        self.dispositivo3 = Dispositivo(3, "memoria", tipo="ram")
        self.dispositivo4 = Dispositivo(4, "placa de red", tipo="wireless", marca="tp-link")

    def compare_dispositivos(self, object1: Dispositivo, object2: Dispositivo):
        if object1.id != object2.id:
            return False
        if object1.nombre != object2.nombre:
            return False
        if object1.marca != object2.marca:
            return False
        if object1.tipo != object2.tipo:
            return False
        return True

    def test_create_database(self):
        database = Database(self.database_template)
        self.assertTrue(self.compare_dispositivos(self.dispositivo1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(self.dispositivo2, database.database[1]))
        self.assertTrue(self.compare_dispositivos(self.dispositivo3, database.database[2]))

    def test_delete_by_id(self):
        database = Database(self.database_template)
        database.delete_by_id(id=2)
        self.assertEqual(len(database.database), 2)
        self.assertTrue(self.compare_dispositivos(self.dispositivo1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(self.dispositivo3, database.database[1]))

    def test_add_dispositivo(self):
        database = Database(self.database_template)
        database.add_dispositivo(self.dispositivo4)
        self.assertEqual(len(database.database), 4)
        self.assertTrue(self.compare_dispositivos(self.dispositivo1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(self.dispositivo2, database.database[1]))
        self.assertTrue(self.compare_dispositivos(self.dispositivo3, database.database[2]))
        self.assertTrue(self.compare_dispositivos(self.dispositivo4, database.database[3]))


if __name__ == '__main__':
    unittest.main()
