from app_flask.config.mysqlconnection import connectToMySQL
from app_flask import BASE_DATOS

class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']

class Amigos:
    def __init__(self, datos):
        self.id = datos['id']
        self.usuario_id = datos['usuario_id']
        self.amigo_id = datos['amigo_id']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']

@classmethod
def agregar_usuario(cls, datos):
        query = """
                INSERT INTO usuarios(nombre, apellido)
                VALUES (%(nombre)s, %(apellido)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)


@classmethod
def crear_amistad(usuario_id, amigo_id):
        query = """
                INSERT INTO amistades(usuario_id, amigo_id)
                VALUES (%s, %s);
                """
        data = (usuario_id, amigo_id)
        return connectToMySQL(BASE_DATOS).query_db(query, data)
