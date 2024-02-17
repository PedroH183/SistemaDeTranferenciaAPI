from run import app
from app.Adapter.LojistaAdapter import LojistaControllerAdapter
from flask import request


@app.route('/lojista/add', methods=["POST"])
def create_usuario_lojista():
    data = request.get_json()
    response = LojistaControllerAdapter.create_lojista(data)
    return response


@app.route("/lojista/update/<int:id>", methods=["PUT"])
def update_usuario_lojista(id):
    data = request.get_json()
    return LojistaControllerAdapter.update_lojista(id, data)


@app.route('/lojista/all', methods=['GET'])
def get_all_lojista():
    return LojistaControllerAdapter.get_all_lojista()


@app.route('/lojista/view/<int:_id>', methods=['GET'])
def get_parent(_id):
    return LojistaControllerAdapter.get_view_lojista(_id)


@app.route('/lojista/delete/<int:_id>', methods=['DELETE'])
def delete_parent(_id):
    return LojistaControllerAdapter.delete_lojista(_id)
