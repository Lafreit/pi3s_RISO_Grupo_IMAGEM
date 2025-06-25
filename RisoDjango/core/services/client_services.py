from .db_connection import MongoDBConnection
import os

def get_db():
    db_name = "riso"
    mongo = MongoDBConnection(db_name=db_name)
    return mongo.get_db()

def replace_special_characters(text):
    replacements = {
       '.': '', '-': '', '(': '', ')': '', ' ': "", "/": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def validate_client_data(data, is_update=False):
    required = ["nome", "documento", "cep", "email"]
    for field in required:
        if not data.get(field):
            raise ValueError("Todos os campos obrigatórios devem ser preenchidos")

    documento = replace_special_characters(data["documento"])
    if not is_update and client_exists(documento):
        raise ValueError("Cliente com este documento já existe")

    nome = data["nome"]
    if len(nome) < 3 or len(nome) > 100 or not replace_special_characters(nome).isalpha():
        raise ValueError("Nome deve conter apenas letras e ter pelo menos 3 caracteres")

    if len(documento) < 11 or not replace_special_characters(documento).isdigit():
        raise ValueError("Documento precisa ter pelo menos 11 números e não pode conter letras")
    
    cep = data["cep"]
    if len(cep.replace('-', "")) != 8 or not replace_special_characters(cep).isdigit():
        raise ValueError("CEP deve conter exatamente 8 dígitos numéricos")

    email = data["email"]
    if "@" not in email:
        raise ValueError("Email inválido")

    telefone = data.get("telefone", "")
    if telefone and not replace_special_characters(telefone).isdigit():
        raise ValueError("Telefone deve conter apenas números")
    
    telefone_residencial = data.get("telefone_residencial", "")
    if telefone_residencial and not replace_special_characters(telefone_residencial).isdigit():
        raise ValueError("Telefone residencial deve conter apenas números")


def create_client(data):
    validate_client_data(data)
    
    client = {
        "nome": data.get("nome"),
        "documento": replace_special_characters(data.get("documento")),
        "cep": replace_special_characters(data.get("cep")),
        "email": data.get("email"),
        "telefone": replace_special_characters(data.get("telefone")),
        "telefone_residencial": replace_special_characters(data.get("telefone_residencial"))
    }

    get_db()["clients"].insert_one(client)
    return True

def get_client(document):
    print(f"Buscando cliente com documento: {document}")
    document = replace_special_characters(document)
    client = get_db()["clients"].find_one({"documento": document})
    return client if client else None

def update_client(document, new_data):
    document = replace_special_characters(document)
    if not get_client(document):
        return False

    validate_client_data(new_data, is_update=True)

    update_fields = {
        "nome": new_data.get("nome"),
        "cep": new_data.get("cep"),
        "email": new_data.get("email"),
        "telefone": new_data.get("telefone"),
        "telefone_residencial": new_data.get("telefone_residencial")
    }

    result = get_db()["clients"].update_one(
        {"documento": document},
        {"$set": update_fields}
    )

    return result.modified_count > 0

def delete_client(document):
    document = replace_special_characters(document)
    result = get_db()["clients"].delete_one({"documento": document})
    return result.deleted_count > 0

def list_clients(skip=0, limit=50):
    clients_cursor = get_db()["clients"].find({}).sort("nome", 1).skip(skip).limit(limit)
    return list(clients_cursor)

def count_clients():
    return get_db()["clients"].count_documents({})

def client_exists(document):
    document = replace_special_characters(document)
    return get_db()["clients"].count_documents({"documento": document}) > 0
