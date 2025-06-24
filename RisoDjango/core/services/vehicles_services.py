from .db_connection import MongoDBConnection
import os

def get_db():
    db_name = "riso"
    mongo = MongoDBConnection(db_name=db_name)
    return mongo.get_db()


def register_vehicle(vehicle_data):
    if not vehicle_exists(vehicle_data.get("placa")):
        vehicle = {
            "tipo": vehicle_data.get("tipo", "carro"),
            "placa": vehicle_data.get("placa"),
            "marca": vehicle_data.get("marca"),
            "modelo": vehicle_data.get("modelo"),
            "ano": vehicle_data.get("ano"),
            "quilometragem": vehicle_data.get("quilometragem", 0),
            "cor": vehicle_data.get("cor", "não especificada"),
            "observacoes": vehicle_data.get("observacoes", ""),
            "documento_cliente": vehicle_data.get("documento_cliente")
        }

        get_db()["vehicles"].insert_one(vehicle)
        return True
    return False

def list_vehicles_by_documento(documento_cliente):
    vehicles = get_db()["vehicles"].find({"documento_cliente": documento_cliente})
    return list(vehicles)


def get_vehicle(placa):
    vehicle = get_db()["vehicles"].find_one({"placa": placa})
    return vehicle if vehicle else None

def update_vehicle(placa, new_data):
    update_fields = {}

    if not vehicle_exists(placa):
        return False
    
    if "tipo" in new_data:
        update_fields["tipo"] = new_data["tipo"]
    if "marca" in new_data:
        update_fields["marca"] = new_data["marca"]
    if "modelo" in new_data:
        update_fields["modelo"] = new_data["modelo"]
    if "ano" in new_data:
        update_fields["ano"] = new_data["ano"]
    if "quilometragem" in new_data:
        update_fields["quilometragem"] = new_data["quilometragem"]
    if "cor" in new_data:
        update_fields["cor"] = new_data["cor"]
    if "observacoes" in new_data:
        update_fields["observacoes"] = new_data["observacoes"]

    result = get_db()["vehicles"].update_one({"placa": placa}, {"$set": update_fields})
    return result.modified_count > 0

def delete_vehicle(placa):
    result = get_db()["vehicles"].delete_one({"placa": placa})
    return result.deleted_count > 0

def list_vehicles():
    vehicles = get_db()["vehicles"].find({}).sort("placa", 1)
    return list(vehicles)

def count_vehicles():
    return get_db()["vehicles"].count_documents({})

def vehicle_exists(placa):
    return get_db()["vehicles"].find_one({"placa": placa}) is not None
