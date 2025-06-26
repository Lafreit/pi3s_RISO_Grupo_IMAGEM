import unittest
from unittest.mock import patch
import mongomock
from core.services import vehicles_services

class TestVehicleServices(unittest.TestCase):

    def setUp(self):
        self.mongo_client = mongomock.MongoClient()
        self.db = self.mongo_client["riso"]

        patcher = patch('core.services.vehicles_services.get_db', return_value=self.db)
        self.mock_get_db = patcher.start()
        self.addCleanup(patcher.stop)

        self.vehicle_data = {
            "tipo": "carro",
            "placa": "ABC1234",
            "marca": "Fiat",
            "modelo": "Uno",
            "ano": 2010,
            "quilometragem": 100000,
            "cor": "vermelho",
            "observacoes": "Sem observações",
            "documento_cliente": "12345678900"
        }

    def test_register_vehicle_success(self):
        result = vehicles_services.register_vehicle(self.vehicle_data)
        self.assertTrue(result)
        self.assertEqual(self.db.vehicles.count_documents({}), 1)

    def test_register_vehicle_duplicate(self):
        vehicles_services.register_vehicle(self.vehicle_data)
      
        result = vehicles_services.register_vehicle(self.vehicle_data)
        self.assertFalse(result)
        self.assertEqual(self.db.vehicles.count_documents({}), 1)

    def test_get_vehicle_found(self):
        self.db.vehicles.insert_one(self.vehicle_data)
        vehicle = vehicles_services.get_vehicle("ABC1234")
        self.assertIsNotNone(vehicle)
        self.assertEqual(vehicle["placa"], "ABC1234")

    def test_get_vehicle_not_found(self):
        vehicle = vehicles_services.get_vehicle("XYZ9999")
        self.assertIsNone(vehicle)

    def test_update_vehicle_success(self):
        self.db.vehicles.insert_one(self.vehicle_data)
        new_data = {
            "marca": "Chevrolet",
            "cor": "azul"
        }
        result = vehicles_services.update_vehicle("ABC1234", new_data)
        self.assertTrue(result)
        updated = self.db.vehicles.find_one({"placa": "ABC1234"})
        self.assertEqual(updated["marca"], "Chevrolet")
        self.assertEqual(updated["cor"], "azul")

    def test_update_vehicle_not_found(self):
        result = vehicles_services.update_vehicle("INEXISTENTE", {"marca": "Ford"})
        self.assertFalse(result)

    def test_list_vehicles_by_documento(self):
        vehicle1 = self.vehicle_data.copy()
        vehicle2 = self.vehicle_data.copy()
        vehicle2["placa"] = "DEF5678"
        vehicle2["documento_cliente"] = "12345678900"
        vehicle3 = self.vehicle_data.copy()
        vehicle3["placa"] = "GHI9012"
        vehicle3["documento_cliente"] = "99999999999"
        self.db.vehicles.insert_many([vehicle1, vehicle2, vehicle3])

        vehicles = vehicles_services.list_vehicles_by_documento("12345678900")
        self.assertEqual(len(vehicles), 2)
        placas = [v["placa"] for v in vehicles]
        self.assertIn("ABC1234", placas)
        self.assertIn("DEF5678", placas)

    def test_filter_vehicles(self):
        vehicles = [
            {"tipo": "carro", "placa": "ABC1234", "modelo": "Uno"},
            {"tipo": "moto", "placa": "MOTO567", "modelo": "Biz"},
            {"tipo": "carro", "placa": "CARRO789", "modelo": "Gol"},
        ]
        self.db.vehicles.insert_many(vehicles)

        filtered = vehicles_services.filter_vehicles({"tipo": "carro"})
        self.assertEqual(len(filtered), 2)

        filtered = vehicles_services.filter_vehicles({"placa": "MOTO"})
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["placa"], "MOTO567")

        filtered = vehicles_services.filter_vehicles({"modelo": "Gol"})
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["modelo"], "Gol")

    def test_delete_vehicle_success(self):
        self.db.vehicles.insert_one(self.vehicle_data)
        result = vehicles_services.delete_vehicle("ABC1234")
        self.assertTrue(result)
        self.assertIsNone(self.db.vehicles.find_one({"placa": "ABC1234"}))

    def test_delete_vehicle_not_found(self):
        result = vehicles_services.delete_vehicle("NADA123")
        self.assertFalse(result)

    def test_list_vehicles(self):
        vehicles = [
            {"placa": "A1"},
            {"placa": "B2"},
            {"placa": "C3"},
        ]
        self.db.vehicles.insert_many(vehicles)
        result = vehicles_services.list_vehicles()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["placa"], "A1") 

    def test_count_vehicles(self):
        self.db.vehicles.insert_many([
            {"placa": "A1"},
            {"placa": "B2"}
        ])
        count = vehicles_services.count_vehicles()
        self.assertEqual(count, 2)

    def test_vehicle_exists(self):
        self.db.vehicles.insert_one(self.vehicle_data)
        self.assertTrue(vehicles_services.vehicle_exists("ABC1234"))
        self.assertFalse(vehicles_services.vehicle_exists("NENHUMA"))

if __name__ == '__main__':
    unittest.main()
