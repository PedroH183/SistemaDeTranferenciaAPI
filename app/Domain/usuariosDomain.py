from run import session
from app.Model.UsuariosLojistaModel import Lojista
from app.Model.UsuariosComunModel import UsuarioComun


class UsuarioService:
  """
    Classe que representa os serviços disponíveis.
    Reponsável por implementar as regras de negocio.
  """

  @classmethod
  def returnAllLojistas(cls):
    return session.query(Lojista).all()
  
  @classmethod
  def returnViewLojista(cls, _id: int):
    return session.query(Lojista).get(_id)

  @classmethod
  def deleteLojista(cls, _id):
    userToDelete = cls.returnViewLojista( _id )
    return session.delete(userToDelete)
  
  @classmethod
  def returnAllUsuarioComun(cls):
    return session.query(UsuarioComun).all() 
  
  @classmethod
  def returnViewUsuarioComun(cls, _id: int):
    return session.query(UsuarioComun).get(_id)

  @classmethod
  def deleteUsuarioComun(cls, _id):
    userToDelete = cls.returnViewUsuarioComun( _id )
    return session.delete(userToDelete)