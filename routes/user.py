from fastapi import APIRouter, Response
from config.db import connection
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet  # encriptación de pass
from starlette.status import HTTP_204_NO_CONTENT

user_router = APIRouter()

# Generación de key aleatorio
key = Fernet.generate_key()
fcript = Fernet(key)


@user_router.get('/users')
def get_users():
    return connection.execute(users.select()).fetchall()


@user_router.post('/users')
def create_users(user: User):
    new_user = {
        "name": user.name,
        "email": user.email
    }
    new_user["password"] = fcript.encrypt(user.password.encode("utf-8"))
    result = connection.execute(users.insert().values(new_user))
    # consultamos y retornamos el último id insertado
    return connection.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user_router.get('/users/{id}')
def get_user_by_id(id: str):
    result = connection.execute(users.select().where(users.c.id == id)).first()
    return result or Response(status_code=HTTP_204_NO_CONTENT)


@user_router.delete('/users/{id}')
def delete_user(id: str):
    result=connection.execute(users.delete().where(users.c.id == id))
    if (result):
        return {
            "message": "Usuario eliminado!"
        }
    else:
        return {
            "message": "Usuario no encontrado"
        }


@user_router.put('/users/{id}')
def update_user(id: str, user: User):
    connection.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=fcript.encrypt(user.password.encode("utf-8"))
    ).where(users.c.id == id))
    return {
      "message": "Usuario actualizado"
    }
