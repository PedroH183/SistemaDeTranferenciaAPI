from flask import jsonify
from app.Domain.usuariosDomain import UsuarioService


class LojistaControllerAdapter:
  
  @staticmethod
  def get_all_lojista():
    Lojista = UsuarioService.returnAllLojistas()
    
    return jsonify([parent.serialize() for parent in Lojista])

  @staticmethod
  def get_view_lojista(_id):
    lojista = UsuarioService.returnViewLojista(_id)
    
    return jsonify( lojista.serialize() if lojista else {"message": "Lojista not found"}  )

  @staticmethod
  def delete_lojista(_id):
    result = UsuarioService.deleteLojista(_id)

    if result:
      return jsonify({"message": "Lojista deleted successfully"})
    else:
      return jsonify({"message": "Lojista not found"}), 404