from .db_connection import MongoDBConnection
import os
from .client_services import get_client
from .vehicles_services import get_vehicle

def get_db():
    db_name = os.environ.get("MONGO_DB_NAME", "riso")
    mongo = MongoDBConnection(db_name=db_name)
    return mongo.get_db()

def service_exists(codigo):
    service = get_db()["servicos"].find_one({"codigo": codigo})
    return service is not None

def register_service(service_data):
    
    if not service_exists(service_data.get("codigo")):
        codigo = service_data.get("codigo")
        tipo = service_data.get("tipo", "padrão")
        descricao = service_data.get("descricao", "")
        preco = service_data.get("preco", 0.0)
        duracao = service_data.get("duracao", 0)
        status = service_data.get("status", "ativo")
        quantidadeRodas = service_data.get("quantidadeRodas", 1)
        prazo = service_data.get("prazo", 0)
        try:
            client_data = get_client(service_data.get("cliente", {}).get("documento", ""))
            vehicle_data = get_vehicle(service_data.get("cliente", {}).get("veiculo", {}).get("placa", ""))
        except Exception as e:
            print(f"Error retrieving client or vehicle data: {e}")
            return False
        if not client_data or not vehicle_data:
            print("Client or vehicle data not found.")
            return False
        service = {
            "codigo": codigo,
            "tipo": tipo,
            "descricao": descricao,
            "preco": preco,
            "prazo": prazo,
            "quantidadeRodas": quantidadeRodas,
            "status": status,
            "duracao": duracao,
            "cliente_documento": client_data.get("documento"),
            "veiculo_placa": vehicle_data.get("placa"),
        }

        get_db()["servicos"].insert_one(service)
        return True
    return False

def get_service(codigo):
    service = get_db()["servicos"].find_one({"codigo": codigo})
    return service if service else None

def update_service(codigo, new_data):
    update_fields = {}
    if not service_exists(codigo):
        return False
    if "tipo" in new_data:
        update_fields["tipo"] = new_data["tipo"]
    if "descricao" in new_data:
        update_fields["descricao"] = new_data["descricao"]
    if "preco" in new_data:
        update_fields["preco"] = new_data["preco"]
    if "prazo" in new_data:
        update_fields["prazo"] = new_data["prazo"]
    if "quantidadeRodas" in new_data:
        update_fields["quantidadeRodas"] = new_data["quantidadeRodas"]
    if "duracao" in new_data:
        update_fields["duracao"] = new_data["duracao"]
    result = get_db()["servicos"].update_one({"codigo": codigo}, {"$set": update_fields})
    return result.modified_count > 0

def delete_service(codigo):
    result = get_db()["servicos"].delete_one({"codigo": codigo})
    return result.deleted_count > 0

def show_services():
    services = get_db()["servicos"].find({})
    return list(services)

def count_services():
    return get_db()["servicos"].count_documents({})

def count_services_by_client_document(document):
    count = get_db()["servicos"].count_documents({"cliente.documento": document})
    return count

def get_active_services():
    active_services = get_db()["servicos"].find({"status": "ativo"})
    return list(active_services)

def get_inactive_services():
    inactive_services = get_db()["servicos"].find({"status": "inativo"})
    return list(inactive_services)

def get_service_by_type(tipo):
    service = get_db()["servicos"].find_one({"tipo": tipo})
    return service if service else None






