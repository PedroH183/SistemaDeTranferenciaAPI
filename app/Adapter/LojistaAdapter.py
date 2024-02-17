from flask import jsonify
from run import session
from app.Services.UsuarioLojistaService import UsuarioLojistaService

# TODO :
# Criar a injeção de dependencia da session nos params das funções !

class LojistaControllerAdapter:

    @staticmethod
    def get_all_lojista():
        lojistas = UsuarioLojistaService.returnAllLojistas()
        return jsonify([loj.to_dict() for loj in lojistas])

    @staticmethod
    def get_view_lojista(_id):
        lojista = UsuarioLojistaService.returnViewLojista(_id)

        return jsonify(lojista.to_dict() if lojista else {"message": "Lojista not found"})

    @staticmethod
    def create_lojista(object):
        return UsuarioLojistaService.create_lojista(object, session)

    @staticmethod
    def delete_lojista(_id):
        return UsuarioLojistaService.deleteLojista(_id)

    @staticmethod
    def update_lojista(id, data):
        return UsuarioLojistaService.update_lojista(data, id, session)
