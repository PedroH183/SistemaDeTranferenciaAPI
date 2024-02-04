
class Usuario:
  """
    Classe que contém a métodos e atributos comuns entre usuarios e lojista.
  """
  __abstract__ = True
  
  def __init__(self, nome_completo, email : str, senha : str, saldo: float = 0):
    self.saldo = saldo
    self.email = email 
    self.senha = senha
    self.nome_completo = nome_completo

  def to_dict(self):
    data = {}
    data["email"] = self.email
    data["id"] = self.id # type: ignore
    data["cpf"] = self.cpf # type: ignore
    data["cnpj"] = self.cnpj # type: ignore
    data["nome_completo"] = self.nome_completo
    
    return data
