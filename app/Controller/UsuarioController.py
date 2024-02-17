from flask import request

from run import app
from app.Adapter.UsuarioAdapter import UsuarioControllerAdapter


@app.route('/usuario/all', methods=['GET'])
def get_all_usuario():
    return UsuarioControllerAdapter.get_all_usuarios()


@app.route("/usuario/add", methods=["POST"])
def create_usuario():
    data = request.get_json()
    return UsuarioControllerAdapter.create_usuario(data)


@app.route("/usuario/update/<int:_id>", methods=["PUT"])
def update_usuario(_id):
    data = request.get_json()
    return UsuarioControllerAdapter.update_usuario(_id, data)


@app.route('/usuario/view/<int:_id>', methods=['GET'])
def view_get_usuario(_id):
    return UsuarioControllerAdapter.get_view_usuario(_id)


@app.route('/usuario/delete/<int:_id>', methods=['DELETE'])
def delete_usuario(_id):
    return UsuarioControllerAdapter.delete_usuario(_id)
