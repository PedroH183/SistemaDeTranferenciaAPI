from run import db

class Genitor(db.Model):
  __tablename__ = 'progenitor'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))

  filhos = db.relationship('Filho', back_populates='genitor')