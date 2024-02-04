from run import Base
from . import UsuarioModel
from sqlalchemy import Column, Integer, String, Float
from app.Domain.transferenciaDomain import ServiceTransferencia


class Lojista(Base, UsuarioModel.Usuario):
  __tablename__ = 'lojista'

  id = Column(Integer, primary_key=True, nullable = False)
  
  saldo = Column(Float, nullable=False)
  senha = Column(String(255) ,nullable=False)
  nome_completo = Column(String(255), nullable=False)
  cnpj   = Column(String(15), unique=True ,nullable=False)
  email = Column(String(255), unique=True ,nullable=False)

  def __init__(self, cnpj : str, email : str, senha : str, nome_completo : str, saldo : float = 0):
    
    self.cnpj = cnpj
    UsuarioModel.__init__(self, nome_completo, email, senha, saldo)

  def transferir_dinheiro(self, quantidade : int, destinatário ):
    return ServiceTransferencia.transferencia_dinheiro(quantidade, self, destinatário)
    
  def to_dict(self):
    return super().to_dict()