from psycopg2 import IntegrityError

from run import session
from app.Domain.Usuarios.UsuariosLojistaModel import Lojista
from app.ReturnClass.ReturnsFactory import SuccessFactory, ExceptionsFactory


class UsuarioLojistaService:
    """
    Classe que representa os serviços disponíveis.
    Reponsável por implementar as regras de negocio.
  """

    @classmethod
    def create_lojista(cls, data, _session):

        user_loja = Lojista(**data)
        try:
            _session.add(user_loja)
            _session.commit()

            return user_loja.to_dict()

        except IntegrityError as err:
            print(str(err))
            return ExceptionsFactory.ExceptionReturn("criar", "lojista")

    @classmethod
    def update_lojista(cls, data, id, _session):
        lojista = cls.returnViewLojista(id)

        if lojista is None:
            return ExceptionsFactory.ExceptionReturn("encontrar", "lojista")

        if data.get("saldo") is not None:
            lojista.saldo = data["saldo"]
        if data.get("senha") is not None:
            lojista.senha = data["senha"]
        if data.get("cnpj") is not None:
            lojista.cnj = data["cnpj"]
        if data.get("email") is not None:
            lojista.email = data["email"]
        if data.get("nome_completo") is not None:
            lojista.nome_completo = data["nome_completo"]

        try:
            _session.commit()
            return SuccessFactory.SuccessReturn("atualizar", "lojista")

        except IntegrityError as err:
            print(err)
            return ExceptionsFactory.ExceptionReturn("atualizar", "lojista")

    @classmethod
    def returnAllLojistas(cls):
        return session.query(Lojista).all()

    @classmethod
    def returnViewLojista(cls, _id: int):
        lojista = session.query(Lojista).get(_id)
        return lojista if lojista is not None else None

    @classmethod
    def deleteLojista(cls, _id):
        userToDelete = cls.returnViewLojista(_id)

        if userToDelete is None:
            return ExceptionsFactory.ExceptionReturn("encontrar", "Lojista")

        session.delete(userToDelete)
        session.commit()
        return SuccessFactory.SuccessReturn("deletado", "Lojista")
