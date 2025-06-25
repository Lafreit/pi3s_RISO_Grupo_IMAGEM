from faker import Faker
from pymongo import MongoClient
import random
from datetime import datetime, timedelta

random.seed(datetime.now().timestamp())

client = MongoClient("mongodb://localhost:27017/")
##db = client["testMongo"]
db = client["riso"]
clientes_collection = db["clients"]
veiculos_collection = db["vehicles"]
servicos_collection = db["servicos"]

fake = Faker("pt_BR")


def replace_special_characters(text):
    replacements = {
        '.': '', '-': '', '(': '', ')': '', ' ': "", "/": "", "+": "", ",": "", "R$": "", "r$": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def validate_client_data(data, is_update=False):
    required = ["nome", "documento", "cep", "email"]
    for field in required:
        if not data.get(field):
            raise ValueError("Todos os campos obrigatórios devem ser preenchidos")

    data["documento"] = replace_special_characters(data["documento"])
    data["cep"] = replace_special_characters(data["cep"])
    data["telefone"] = replace_special_characters(data.get("telefone", ""))
    data["telefone_residencial"] = replace_special_characters(data.get("telefone_residencial", ""))

    nome = data["nome"]
    if len(nome) < 3 or len(nome) > 100 or not replace_special_characters(nome).replace(" ", "").isalpha():
        raise ValueError("Nome deve conter apenas letras e ter entre 3 e 100 caracteres")

    if len(data["documento"]) < 11 or not data["documento"].isdigit():
        raise ValueError("Documento precisa ter pelo menos 11 números e não conter letras")

    if len(data["cep"]) != 8 or not data["cep"].isdigit():
        raise ValueError("CEP deve conter exatamente 8 dígitos numéricos")

    if "@" not in data["email"]:
        raise ValueError("Email inválido")

    if data["telefone"] and not data["telefone"].isdigit():
        raise ValueError("Telefone deve conter apenas números")

    if data["telefone_residencial"] and not data["telefone_residencial"].isdigit():
        raise ValueError("Telefone residencial deve conter apenas números")

    return data 

def gerar_cliente():
    return {
        "nome": fake.name(),
        "documento": fake.cpf(),
        "cep": fake.postcode(),
        "email": fake.email(),
        "telefone": fake.phone_number(),
        "telefone_residencial": fake.phone_number() if random.random() > 0.5 else ""
    }

def gerar_veiculo(documento_cliente):
    return {
        "tipo": random.choice(["Carro", "Moto", "Caminhão"]),
        "placa": fake.license_plate(),
        "marca": fake.company(),
        "modelo": fake.word().capitalize(),
        "ano": str(fake.year()),
        "quilometragem": str(random.randint(10000, 200000)),
        "cor": fake.color_name(),
        "observacoes": fake.sentence(),
        "documento_cliente": documento_cliente
    }

def gerar_servico(cliente, veiculo):
    data_inicio = datetime.now() - timedelta(days=random.randint(0, 30))
    duracao_horas = random.randint(1, 5)
    data_inicio += timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))

    data_inicio_str = datetime.fromisoformat(data_inicio.isoformat())
    data_fechamento_str =  data_inicio_str + timedelta(hours=duracao_horas)
    prazo_execucao_str  =  datetime.fromisoformat(data_inicio.isoformat())

    return {
        "codigo": random.randint(1000, 9999),
        "tipo": random.choice(["Desamaçar Roda", "Pintura", "Revisão Completa", "Troca de Óleo"]),
        "descricao": fake.text(max_nb_chars=50),
        "preco": random.randint(100, 1000),
        "prazo_execucao": prazo_execucao_str,
        "quantidadeRodas": random.randint(1, 4),
        "status": random.choice(["ativo", "cancelado", "finalizado"]),
        "duracao": f"{duracao_horas}:00",
        "data_inicio": data_inicio_str,
        "cliente": cliente,
        "veiculo": veiculo,
        "data_fechamento": data_fechamento_str
    }

## gera quanto numeros quiser
n = 2000

for _ in range(n):
    try:
        cliente_data = gerar_cliente()
        cliente_validado = validate_client_data(cliente_data)
        cliente_validado["_id"] = clientes_collection.insert_one(cliente_validado).inserted_id

        veiculos = []
        for _ in range(random.randint(1, 3)):
            veiculo = gerar_veiculo(cliente_validado["documento"])
            veiculo["_id"] = veiculos_collection.insert_one(veiculo).inserted_id
            veiculos.append(veiculo)

        for veiculo in veiculos:
            for _ in range(random.randint(0, 5)):
                servico = gerar_servico(cliente_validado, veiculo)
                servicos_collection.insert_one(servico)
    except ValueError as e:
        print(f"Erro ao validar cliente: {e}")
        continue

print(f"Inseridos até {n} clientes com seus respectivos veículos e serviços (0-5 por veículo) com sucesso.")
