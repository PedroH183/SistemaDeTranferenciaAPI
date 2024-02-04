from run import session
from app.Model.UsuariosLojistaModel import Lojista
from app.Model.UsuariosComunModel import UsuarioModel


class UsuarioService:
  """
    Classe que representa os serviços disponíveis.
    Reponsável por implementar as regras de negocio.
  """

  @classmethod
  def returnAllLojistas(self):
    return session.query(Lojista).all()
  
  @classmethod
  def returnViewLojista(self, _id: int):
    return session.query(Lojista).get(_id)

  @classmethod
  def deleteLojista(self, _id):
    userToDelete = self.returnViewLojista( _id )
    return session.delete(userToDelete)
  
  @classmethod
  def returnAllUsuarioComun(self):
    return session.query(UsuarioModel).all()
  
  @classmethod
  def returnViewUsuarioComun(self, _id: int):
    return session.query(UsuarioModel).get(_id)

  @classmethod
  def deleteUsuarioComun(self, _id):
    userToDelete = self.returnViewUsuarioComun( _id )
    return session.delete(userToDelete)