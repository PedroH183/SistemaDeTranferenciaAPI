from typing import Optional
from pydantic import BaseModel


class UsuarioAddSchema(BaseModel):
  cpf : str
  senha : str
  saldo : float
  email : str
  nome_completo : str


class UsuarioEditSchema(BaseModel):
  cpf : Optional[str] = None
  senha : Optional[str] = None
  email : Optional[str] = None
  saldo : Optional[float] = None
  nome_completo : Optional[str] = None