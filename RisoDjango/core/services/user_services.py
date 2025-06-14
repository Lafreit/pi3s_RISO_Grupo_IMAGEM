import bcrypt
from .db_connection import MongoDBConnection
import os

def get_db():
    db_name = os.environ.get("MONGO_DB_NAME", "riso")
    mongo = MongoDBConnection(db_name=db_name)
    return mongo.get_db()

def verify_user(username):
    
    user = get_db()["users"].find_one({"username": username})
    return user is not None 

def create_user(username, password):
    if not verify_user(username):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = {
            "username": username,
            "password": hashed
        }
        get_db()["users"].insert_one(user)
        return True
    return False

def auth_user(username, password):
    
    user = get_db()["users"].find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return True
    return False

def auth_session(session):
    if (not session.get('session', False) or
        not session.get('username', None)):
        return False
    if session.get('session') != 'active':
        return False
    return True
    

def get_user(username):
    
    user = get_db()["users"].find_one({"username": username})
    return user if user else None

def update_user(username, new_data):
    

    if "password" in new_data:
        new_data["password"] = bcrypt.hashpw(new_data["password"].encode('utf-8'), bcrypt.gensalt())

    result = get_db()["users"].update_one({"username": username}, {"$set": new_data})
    return result.modified_count > 0

def delete_user(username):
    
    result = get_db()["users"].delete_one({"username": username})
    return result.deleted_count > 0

def show_users():
    
    usuarios = get_db()["users"].find({}, {"password": 0})
    return list(usuarios)

def count_users():
    
    return get_db()["users"].count_documents({})
