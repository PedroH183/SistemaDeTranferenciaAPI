from flask import jsonify
from app.Domain.usuariosDomain import UsuarioService


class UsuarioControllerAdapter:
  
  @staticmethod
  def get_all_usuarios():
    usuarios = UsuarioService.returnAllUsuarioComun()
    
    return jsonify([user.to_dict() for user in usuarios])

  @staticmethod
  def get_view_usuario(_id):
    user = UsuarioService.returnViewUsuarioComun(_id)
    
    return jsonify( user.to_dict() if user else {"message": "Usuario not found"}  )

  @staticmethod
  def delete_usuario(_id):
    result = UsuarioService.deleteUsuarioComun(_id)

    if result:
      return jsonify({"message": "Usuario deleted successfully"})
    else:
      return jsonify({"message": "Usuario not found"}), 404