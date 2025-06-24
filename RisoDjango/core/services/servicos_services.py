from .db_connection import MongoDBConnection
import os
from .client_services import get_client
from .vehicles_services import get_vehicle
from datetime import datetime

def get_db():
    db_name = "riso"
    mongo = MongoDBConnection(db_name=db_name)
    return mongo.get_db()

def service_exists(codigo):
    codigo = int(codigo)
    service = get_db()["servicos"].find_one({"codigo": codigo})
    return service is not None

def register_service(service_data):
    print("Registrando serviço...")
    codigo = int(get_last_service_code())
    if codigo is None:
        codigo = 1
    else:
        codigo += 1
    if not service_exists(codigo):
        tipo = service_data.get("tipo", "padrão")
        descricao = service_data.get("descricao", "")
        preco = service_data.get("preco", 0.0)
        duracao = service_data.get("duracao", 0)
        status = service_data.get("status", "ativo")
        quantidadeRodas = service_data.get("quantidadeRodas", 1)
        prazo = service_data.get("prazo_execucao", 0)
        dataInicio = service_data.get("data_inicio", None)
        try:
            client_data = get_client(service_data.get("documento_cliente"))
            vehicle_data = get_vehicle(service_data.get("placa_veiculo"))
        except Exception as e:
            print(f"Erro ao buscar cliente ou veículo: {e}")
            return False
        if not client_data or not vehicle_data:
            print("Cliente ou veículo não encontrado.")
            return False
        service = {
            "codigo": codigo,
            "tipo": tipo,
            "descricao": descricao,
            "preco": preco,
            "prazo_execucao": prazo,
            "quantidadeRodas": quantidadeRodas,
            "status": status,
            "duracao": duracao,
            "data_inicio": dataInicio,
            "cliente": client_data,
            "veiculo": vehicle_data,
        }

        get_db()["servicos"].insert_one(service)
        return True
    return False

def get_service(codigo):
    codigo = int(codigo)
    service = get_db()["servicos"].find_one({"codigo": codigo})
    return service if service else None

def get_last_service_code():
    last_service = get_db()["servicos"].find_one({}, sort=[("codigo", -1)])
    return last_service["codigo"] if last_service else None

def update_service(codigo, new_data):
    update_fields = {}
    codigo = int(codigo)
    if not service_exists(codigo):
        return False
    if "tipo" in new_data:
        update_fields["tipo"] = new_data["tipo"]
    if "descricao" in new_data:
        update_fields["descricao"] = new_data["descricao"]
    if "preco" in new_data:
        update_fields["preco"] = new_data["preco"]
    if "prazo_execucao" in new_data:
        update_fields["prazo_execucao"] = new_data["prazo_execucao"]
    if "quantidadeRodas" in new_data:
        update_fields["quantidadeRodas"] = new_data["quantidadeRodas"]
    if "status" in new_data:
        update_fields["status"] = new_data["status"]
    if "duracao" in new_data:
        update_fields["duracao"] = new_data["duracao"]
    if "data_inicio" in new_data:
        update_fields["data_inicio"] = new_data["data_inicio"]

    result = get_db()["servicos"].update_one({"codigo": codigo}, {"$set": update_fields})
    return result.modified_count > 0

def delete_service(codigo):
    result = get_db()["servicos"].delete_one({"codigo": codigo})
    return result.deleted_count > 0

def show_services():
    services = get_db()["servicos"].find({"status": "ativo"}).sort('prazo', 1)
    return list(services)

def show_completed_services():
    completed_services = get_db()["servicos"].find({"status": "finalizado"}).sort('prazo', 1)
    return list(completed_services)

def show_canceled_services():
    canceled_services = get_db()["servicos"].find({"status": "cancelado"}).sort('prazo', 1)
    return list(canceled_services)

def count_services():
    return get_db()["servicos"].count_documents({})

def count_services_by_client_document(document):
    count = get_db()["servicos"].count_documents({"cliente.documento": document})
    return count

def get_open_services_by_client_document(document):
    open_services = get_db()["servicos"].find({"cliente.documento": document, "status": "ativo"})
    return list(open_services)

def get_completed_services_by_client_document(document):
    completed_services = get_db()["servicos"].find({"cliente.documento": document, "status": "finalizado"})
    return list(completed_services)

def get_active_services():
    active_services = get_db()["servicos"].find({"status": "ativo"})
    return list(active_services)

def get_inactive_services():
    inactive_services = get_db()["servicos"].find({"status": "inativo"})
    return list(inactive_services)

def get_service_by_type(tipo):
    service = get_db()["servicos"].find_one({"tipo": tipo})
    return service if service else None

def finish_service(codigo):
    codigo = int(codigo)
    result = get_db()["servicos"].update_one({"codigo": codigo}, {"$set": {"status": "finalizado", "data_fechamento": datetime.now()}})
    return result.modified_count > 0

def cancel_service(codigo):
    codigo = int(codigo)
    result = get_db()["servicos"].update_one({"codigo": codigo}, {"$set": {"status": "cancelado", "data_fechamento": datetime.now()}})
    return result.modified_count > 0

def show_delayed_services():
    today = datetime.now()
    delayed_services = get_db()["servicos"].find({"status": "ativo", "prazo": {"$lt": today}})
    return list(delayed_services)

def get_next_due_service():
    next_due_service = get_db()["servicos"].find_one({"status": "ativo", "prazo": {"$gt": datetime.now()}}, sort=[("prazo", 1)])
    return next_due_service if next_due_service else None

def get_month_service_count(start_date, end_date):
    count = get_db()["servicos"].count_documents({
        "data_inicio": {"$gte": start_date, "$lt": end_date}
    })
    return count




