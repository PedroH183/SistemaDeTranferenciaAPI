from run import db
from app.Model.GenitorTable import Genitor 

class ParentService:
  """
    Classe que representa os serviços disponíveis.
    Reponsável por implementar as regras de negocio.
  """

  @classmethod
  def returnAllParents(self):
    return db.session.query(Genitor).all()
  
  @classmethod
  def returnViewParent(self, _id: int):
    return db.session.query(Genitor).get(_id)

  @classmethod
  def deleteParent(self, _id):
    userToDelete = self.returnViewParent( _id )
    return db.session.delete(userToDelete)