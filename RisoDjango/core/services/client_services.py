from .db_connection import MongoDBConnection
import os

def get_db():
    db_name = os.environ.get("MONGO_DB_NAME", "riso")
    mongo = MongoDBConnection(db_name=db_name)
    return mongo.get_db()

def replace_special_characters(text):
    replacements = {
       '.': '', '-': '', '(': '', ')': '', ' ': "", "/": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def validate_client_data(data):
    required = ["nome", "documento", "cep", "email"]
    for field in required:
        if not data.get(field):
            raise ValueError("Todos os campos obrigatórios devem ser preenchidos")

    if client_exists(data["documento"]):
        raise ValueError("Cliente com este documento já existe")

    nome = data["nome"]
    if len(nome) < 3 or len(nome) > 100 or not replace_special_characters(nome).isalpha():
        raise ValueError("Nome deve conter apenas letras e ter pelo menos 3 caracteres")

    documento = data["documento"]
    if len(documento) < 11 or not replace_special_characters(documento).isdigit():
        raise ValueError("Documento precisa ter pelo menos 11 numeros e não pode conter letras")
    
    cep = data["cep"]
    if len(cep.replace('-',"")) != 8 or not replace_special_characters(cep).isdigit():
        raise ValueError("CEP deve conter exatamente 8 dígitos numéricos")

    email = data["email"]
    if "@" not in email:
        raise ValueError("Email inválido")

    telefone = data['telefone']
    if "telefone" in data and data["telefone"] and not replace_special_characters(data["telefone"]).isdigit():
        raise ValueError("Telefone deve conter apenas numeros")
    
    telefone_residencial = data['telefone_residencial']
    if "telefone_residencial" in data and data["telefone_residencial"] and not replace_special_characters(data["telefone_residencial"]).isdigit():
        raise ValueError("Telefone residencial deve conter apenas numeros")


def create_client(data):
    validate_client_data(data)

    client = {
        "nome": data.get("nome"),
        "documento": data.get("documento"),
        "cep": data.get("cep"),
        "email": data.get("email"),
        "telefone": data.get("telefone"),
        "telefone_residencial": data.get("telefone_residencial")
    }

    get_db()["clients"].insert_one(client)
    return True

def get_client(document):
    client = get_db()["clients"].find_one({"documento": document})
    return client if client else None

def update_client(document, new_data):
    update_fields = {}

    if not get_client(document):
        return False
    
    if "nome" in new_data:
        update_fields["nome"] = new_data["nome"]
    if "cep" in new_data:
        update_fields["cep"] = new_data["cep"]
    if "email" in new_data:
        update_fields["email"] = new_data["email"]
    if "telefone" in new_data:
        update_fields["telefone"] = new_data["telefone"]
    if "telefone_residencial" in new_data:
        update_fields["telefone_residencial"] = new_data["telefone_residencial"]

    result = get_db()["clients"].update_one({"documento": document}, {"$set": update_fields})
    return True if result.modified_count > 0 else False

def delete_client(document):
    result = get_db()["clients"].delete_one({"documento": document})
    return result.deleted_count > 0

def list_clients():
    clients = get_db()["clients"].find({})
    return list(clients)

def count_clients():
    return get_db()["clients"].count_documents({})

def client_exists(document):
    client = get_db()["clients"].find_one({"documento": document})
    if client:
        return True
    return False