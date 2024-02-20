from typing import Optional
from pydantic import BaseModel


class LojistaAddSchema(BaseModel):
  cnpj : str
  senha : str
  saldo : float
  email : str
  nome_completo : str


class LojistaEditSchema(BaseModel):
  cnpj : Optional[str] = None
  senha : Optional[str] = None
  email : Optional[str] = None
  saldo : Optional[float] = None
  nome_completo : Optional[str] = None