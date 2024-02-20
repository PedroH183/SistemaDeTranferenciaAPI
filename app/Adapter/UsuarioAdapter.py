from run import session
from flask import jsonify
from app.Domain.Usuarios.UsuariosComumModel import UsuarioComum
from app.Services.UsuarioComumService import UsuarioComumService


class UsuarioControllerAdapter:

    @staticmethod
    def get_all_usuarios():
        usuarios: list[UsuarioComum] = UsuarioComumService.returnAllUsuarioComum()

        return jsonify([user.to_dict() for user in usuarios])

    @staticmethod
    def create_usuario(data):
        return UsuarioComumService.createUsuarioComum(data, session)

    @staticmethod
    def get_view_usuario(_id):
        user = UsuarioComumService.returnViewUsuarioComum(_id)
        return jsonify(user.to_dict() if user else {"message": "Usuario not found"})

    @staticmethod
    def update_usuario(_id, data):
        return UsuarioComumService.updateUsuarioComum(_id, data, session)

    @staticmethod
    def delete_usuario(_id):
        return UsuarioComumService.deleteUsuarioComum(_id)

    @staticmethod
    def transferirDinheiro(data_request : dict):
        return UsuarioComumService.transferencia(data_request)