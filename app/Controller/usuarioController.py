from run import app
from app.Adapter.usuarioAdapter import UsuarioControllerAdapter


@app.route('/usuario/all', methods=['GET'])
def get_all_usuario():
    return UsuarioControllerAdapter.get_view_usuario()

@app.route('/usuario/<int:_id>', methods=['GET'])
def view_get_usuario(_id):
    return UsuarioControllerAdapter.get_view_usuario(_id)

@app.route('/usuario/<int:_id>', methods=['DELETE'])
def delete_usuario(_id):
    return UsuarioControllerAdapter.delete_usuario(_id)