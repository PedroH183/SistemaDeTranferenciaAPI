from flask import jsonify
from app.Domain.parentsDomain import ParentService


class ParentControllerAdapter:
  
  @staticmethod
  def get_all_parents():
    parents = ParentService.returnAllParents()
    
    return jsonify([parent.serialize() for parent in parents])

  @staticmethod
  def get_parent(_id):
    parent = ParentService.returnViewParent(_id)
    
    if parent:
      return jsonify(parent.serialize())
    else:
      return jsonify({"message": "Parent not found"}), 404

  @staticmethod
  def delete_parent(_id):
    result = ParentService.deleteParent(_id)

    if result:
      return jsonify({"message": "Parent deleted successfully"})
    else:
      return jsonify({"message": "Parent not found"}), 404