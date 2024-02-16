from run import Base
from sqlalchemy import Column, Integer, String, Float


class Lojista(Base):
    __tablename__ = 'lojista'

    id = Column(Integer, primary_key=True, nullable=False)

    saldo = Column(Float, nullable=False)
    senha = Column(String(255), nullable=False)
    nome_completo = Column(String(255), nullable=False)
    cnpj = Column(String(20), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    def __init__(self, cnpj: str, email: str, senha: str, nome_completo: str, saldo: float = 0):

        self.senha = senha
        self.cnpj = cnpj
        self.email = email
        self.saldo = saldo
        self.nome_completo = nome_completo

    def to_dict(self):
        data = {
            "id": self.id,
            "cnpj": self.cnpj,
            "saldo": self.saldo,
            "email": self.email,
            "nome_completo": self.nome_completo
        }
        return data
