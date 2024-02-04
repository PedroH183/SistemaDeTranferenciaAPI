from run import Base
from . import UsuarioModel
from sqlalchemy import Column, Integer, String, Float
from app.Domain.transferenciaDomain import ServiceTransferencia


class UsuarioComun(Base, UsuarioModel.Usuario):
  __tablename__ = 'usuario_comun'

  id = Column(Integer, primary_key=True, nullable = False)
  
  saldo = Column(Float, nullable=False)
  senha = Column(String(255),nullable=False)
  nome_completo = Column(String(255), nullable=False)
  cpf   = Column(String(15), unique=True ,nullable=False)
  email = Column(String(255), unique=True ,nullable=False)

  def __init__(self, cpf : str, email : str, senha : str, nome_completo : str, saldo : float = 0):
    
    self.cpf = cpf
    UsuarioModel.__init__(self, nome_completo, cpf, email, senha, saldo)

  def transferir_dinheiro(self, quantidade : int, destinatario ):
    return ServiceTransferencia.transferencia_dinheiro(quantidade, self, destinatario)
    
  def to_dict(self):
    return super().to_dict()
