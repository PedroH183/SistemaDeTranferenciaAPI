from statistics import quantiles
from psycopg2 import IntegrityError
from app.Domain.Usuarios.UsuariosLojistaModel import Lojista
from app.Services.UsuarioLojistaService import UsuarioLojistaService

from run import session
from app.Domain.Usuarios.UsuariosComumModel import UsuarioComum
from app.ReturnClass.ReturnsFactory import ExceptionsFactory, SuccessFactory


class UsuarioComumService:
    """
    Classe que representa os serviços disponíveis para um usuario comum.
    Reponsável por implementar as regras de negocio.
  """

    serviceLojista : UsuarioLojistaService = UsuarioLojistaService()

    @classmethod
    def createUsuarioComum(cls, data, _session):

        usuario = UsuarioComum(**data)
        try:
            _session.add(usuario)
            _session.commit()

            return usuario.to_dict()

        except IntegrityError as err:
            print(err)
            return ExceptionsFactory.ExceptionReturn("criar", "Usuario")

    @classmethod
    def updateUsuarioComum(cls, _id, data, _session):
        usuario = cls.returnViewUsuarioComum(_id)

        if usuario is None:
            return ExceptionsFactory.ExceptionReturn("encontrar", "usuario")

        if data.get("saldo") is not None:
            usuario.saldo = data["saldo"]
        if data.get("senha") is not None:
            usuario.senha = data["senha"]
        if data.get("cpf") is not None:
            usuario.cpf = data["cpf"]
        if data.get("email") is not None:
            usuario.email = data["email"]
        if data.get("nome_completo") is not None:
            usuario.nome_completo = data["nome_completo"]

        try:
            _session.commit()
            return SuccessFactory.SuccessReturn("atualizar", "lojista")

        except IntegrityError as err:
            print(err)
            return ExceptionsFactory.ExceptionReturn("atualizar", "lojista")

    @classmethod
    def returnAllUsuarioComum(cls) -> list[UsuarioComum]:
        return session.query(UsuarioComum).all()

    @classmethod
    def returnViewUsuarioComum(cls, _id: int) -> UsuarioComum:
        usuario = session.query(UsuarioComum).get(_id)
        return usuario if usuario is not None else None

    @classmethod
    def deleteUsuarioComum(cls, _id: int):
        userToDelete = cls.returnViewUsuarioComum(_id)

        if userToDelete is None:
            return ExceptionsFactory.ExceptionReturn("encontrar", "Usuario Comum")

        session.delete(userToDelete)
        session.commit()
        return SuccessFactory.SuccessReturn("deletado", "Usuario Comum")

    @classmethod
    def transferencia(cls, data_request : dict):        

        quantidade = data_request.get("quantidade")
        remetente_id = data_request.get("remetente_id")
        destinatario_id = data_request.get("destinatario_id")

        if quantidade is None:
            return ExceptionsFactory.ExceptionReturn("transferir", "o dinheiro, saldo insuficiente!")

        if None in [remetente_id, destinatario_id]:
            return ExceptionsFactory.ExceptionReturn("transferir", "o dinheiro, alguma das credenciais é/são inválidas")

        destinatario_instance : UsuarioComum | Lojista = cls.returnViewUsuarioComum(destinatario_id)
        remetente_instance : UsuarioComum = cls.returnViewUsuarioComum(remetente_id)

        if destinatario_instance is None:
            destinatario_instance = cls.serviceLojista.returnViewLojista(destinatario_id)

        if None in [destinatario_instance, remetente_instance]:
            return ExceptionsFactory.ExceptionReturn("transferir", "o dinheiro, um ou mais usuários não identificados!")

        return remetente_instance.transferir_dinheiro(quantidade, destinatario_instance)