import unittest
from unittest.mock import patch
from core.services import client_services
import mongomock


class TestClientService(unittest.TestCase):

    def setUp(self):
        self.mongo_client = mongomock.MongoClient()
        self.db = self.mongo_client["riso"]

        patcher = patch('core.services.client_services.get_db', return_value=self.db)
        self.mock_get_db = patcher.start()
        self.addCleanup(patcher.stop)

    def test_create_client_success(self):
        data = {
            "nome": "Joao Silva",
            "documento": "123.456.789-00",
            "cep": "12345-678",
            "email": "joao@email.com",
            "telefone": "(11) 98765-4321",
            "telefone_residencial": "(11) 1234-5678"
        }
        result = client_services.create_client(data)
        self.assertTrue(result)
        self.assertEqual(self.db.clients.count_documents({}), 1)

    def test_create_client_duplicate_document(self):
        data = {
            "nome": "Maria Souza",
            "documento": "123.456.789-00",
            "cep": "12345-678",
            "email": "maria@email.com",
            "telefone": "(11) 99999-8888",
            "telefone_residencial": ""
        }
        client_services.create_client(data)
        with self.assertRaises(ValueError):
            client_services.create_client(data)

    def test_get_client(self):
        doc = "12345678900"
        self.db.clients.insert_one({
            "nome": "Teste",
            "documento": doc,
            "cep": "12345678",
            "email": "teste@email.com",
            "telefone": "11999998888",
            "telefone_residencial": "1112345678"
        })
        result = client_services.get_client("123.456.789-00")
        self.assertIsNotNone(result)
        self.assertEqual(result["nome"], "Teste")


    def test_delete_client(self):
        doc = "12345678900"
        self.db.clients.insert_one({
            "nome": "Para Deletar",
            "documento": doc,
            "cep": "12345678",
            "email": "delete@email.com",
            "telefone": "",
            "telefone_residencial": ""
        })
        result = client_services.delete_client("123.456.789-00")
        self.assertTrue(result)
        self.assertIsNone(self.db.clients.find_one({"documento": doc}))

    def test_list_clients(self):
        self.db.clients.insert_many([
            {"nome": "Ana", "documento": "1"},
            {"nome": "Bruno", "documento": "2"},
        ])
        clients = client_services.list_clients()
        self.assertEqual(len(clients), 2)

    def test_list_filtered_clients_by_name(self):
        self.db.clients.insert_many([
            {"nome": "Carlos", "documento": "111"},
            {"nome": "Carla", "documento": "222"},
            {"nome": "Joana", "documento": "333"}
        ])
        filters = {"nome": "Carl", "documento": ""}
        result = client_services.list_filtered_clients(filters)
        self.assertEqual(len(result), 2)

    def test_count_clients(self):
        self.db.clients.insert_many([
            {"nome": "X", "documento": "1"},
            {"nome": "Y", "documento": "2"}
        ])
        count = client_services.count_clients()
        self.assertEqual(count, 2)


if __name__ == '__main__':
    unittest.main()
