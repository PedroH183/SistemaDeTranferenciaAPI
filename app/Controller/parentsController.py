from run import app
from ..Adapter.parentsAdapter import ParentControllerAdapter


@app.route('/parents/all', methods=['GET'])
def get_all_parents():
    return ParentControllerAdapter.get_all_parents()

@app.route('/parents/<int:_id>', methods=['GET'])
def get_parent(_id):
    return ParentControllerAdapter.get_parent(_id)

@app.route('/parents/<int:_id>', methods=['DELETE'])
def delete_parent(_id):
    return ParentControllerAdapter.delete_parent(_id)