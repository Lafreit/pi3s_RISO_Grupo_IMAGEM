from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.services import client_services
from core.services.db_connection import MongoDBConnection
from unittest.mock import patch
import unittest

class ClientViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.client_data = {
            "nome": "Cliente Teste",
            "documento": "123.456.789-00",
            "cep": "13500-000",
            "email": "cliente@teste.com",
            "telefone": "(11)99999-9999",
            "telefone_residencial": "(11)3333-3333"
        }
        with patch('core.services.client_services.get_db', side_effect=self.fake_get_db):
            client_services.create_client(self.client_data)

    @staticmethod
    def fake_get_db():
        return MongoDBConnection(db_name="testMongo").get_db()

    def tearDown(self):
        with patch('core.services.client_services.get_db', side_effect=self.fake_get_db):
            client_services.delete_client(self.client_data["documento"])

    @patch('core.services.client_services.get_db', side_effect=fake_get_db)
    def test_cadastro_cliente_get(self, mock_db):
        response = self.client.get(reverse('cadastro_cliente'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro_cliente.html')

    @patch('core.services.client_services.get_db', side_effect=fake_get_db)
    def test_cadastro_cliente_post(self, mock_db):
        data = self.client_data.copy()
        data["documento"] = "987.654.321-00"
        response = self.client.post(reverse('cadastro_cliente'), data)
        self.assertEqual(response.status_code, 302)
        self.assertIn('vizualizar_cliente', response.url)
        with patch('core.services.client_services.get_db', side_effect=self.fake_get_db):
            client_services.delete_client(data["documento"])

    @patch('core.services.client_services.get_db', side_effect=fake_get_db)
    def test_listar_clientes(self, mock_db):
        response = self.client.get(reverse('listar_clientes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_clientes.html')
        self.assertIn('clients', response.context)

    @patch('core.services.client_services.get_db', side_effect=fake_get_db)
    def test_editar_cliente_get(self, mock_db):
        response = self.client.get(reverse('editar_cliente') + f'?documento={self.client_data["documento"]}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_cliente.html')

    @patch('core.services.client_services.get_db', side_effect=fake_get_db)
    def test_editar_cliente_post(self, mock_db):
        data = self.client_data.copy()
        data["nome"] = "Cliente Editado"
        response = self.client.post(reverse('editar_cliente'), data)
        self.assertEqual(response.status_code, 302)
        self.assertIn('listar_clientes', response.url)

    @patch('core.services.client_services.get_db', side_effect=fake_get_db)
    def test_excluir_cliente_get(self, mock_db):
        response = self.client.get(reverse('excluir_cliente') + f'?documento={self.client_data["documento"]}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'excluir_cliente.html')

    @patch('core.services.client_services.get_db', side_effect=fake_get_db)
    def test_excluir_cliente_post(self, mock_db):
        data = self.client_data.copy()
        data["documento"] = "000.000.000-00"
        with patch('core.services.client_services.get_db', side_effect=self.fake_get_db):
            client_services.create_client(data)
        response = self.client.post(reverse('excluir_cliente'), {"documento": data["documento"]})
        self.assertEqual(response.status_code, 302)
        self.assertIn('listar_clientes', response.url)
        with patch('core.services.client_services.get_db', side_effect=self.fake_get_db):
            client_services.delete_client(data["documento"])

    @patch('core.services.client_services.get_db', side_effect=fake_get_db)
    def test_vizualizar_cliente(self, mock_db):
        response = self.client.get(reverse('vizualizar_cliente') + f'?documento={self.client_data["documento"]}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vizualizar_cliente.html')
        self.assertIn('client', response.context)

if __name__ == "__main__":
    unittest.main()
