from run import app
from app.Adapter.lojistaAdapter import LojistaControllerAdapter


@app.route('/lojista/all', methods=['GET'])
def get_all_lojista():
    return LojistaControllerAdapter.get_all_lojista()

@app.route('/lojista/<int:_id>', methods=['GET'])
def get_parent(_id):
    return LojistaControllerAdapter.get_view_lojista(_id)

@app.route('/lojista/<int:_id>', methods=['DELETE'])
def delete_parent(_id):
    return LojistaControllerAdapter.delete_lojista(_id)