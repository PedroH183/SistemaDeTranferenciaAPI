from run import db

class Filho(db.Model):
  __tablename__ = 'filho'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  
  # relação de um para muitos 
  parent_id = db.Column(db.Integer, db.ForeignKey('progenitor.id'))
  genitor = db.relationship('Genitor', back_populates='filhos')