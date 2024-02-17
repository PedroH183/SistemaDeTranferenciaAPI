from run import Base
from sqlalchemy import Column, Integer, String, Float
from app.Domain.Transferencia.transferenciaDomain import ServiceTransferencia


class UsuarioComum(Base):
    __tablename__ = 'usuario_comum'

    id = Column(Integer, primary_key=True, nullable=False)

    saldo = Column(Float, nullable=False)
    senha = Column(String(255), nullable=False)
    nome_completo = Column(String(255), nullable=False)
    cpf = Column(String(15), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    def __init__(self, cpf: str, email: str, senha: str, nome_completo: str, saldo: float = 0):

        self.cpf = cpf
        self.senha = senha
        self.email = email
        self.saldo = saldo
        self.nome_completo = nome_completo

    def to_dict(self):
        data = {
            "id": self.id,
            "cpf": self.cpf,
            "saldo": self.saldo,
            "email": self.email,
            "nome_completo": self.nome_completo
        }
        return data

    def transferir_dinheiro(self, quantidade: int, destinatario):
        return ServiceTransferencia.transferencia_dinheiro(quantidade, self, destinatario)
