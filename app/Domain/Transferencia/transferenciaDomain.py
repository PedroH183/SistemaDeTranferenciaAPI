import json
import requests
from app.ReturnClass.ReturnsFactory import ExceptionsFactory, SuccessFactory
from run import session


class ServiceTransferencia:
  """
    Classe responsável por fazer o envio de dinheiro para outra conta.

    Encapsula as logica de :
      Verificação de saldo, Existencia de usuario, Transferencia do dinheiro
  """

  @classmethod
  def transferencia_dinheiro(cls, quantidade: float, remetente, beneficiario):
    if remetente is beneficiario:
      return ExceptionsFactory.ExceptionReturn("transferir", "dinheiro, dados redundantes!", 403)

    if not cls.__check_saldo_remetente(remetente, quantidade):
      return ExceptionsFactory.ExceptionReturn("transferir", "dinheiro, saldo insuficiente", 403)

    checking_api_transfer = requests.get("https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc")
    validator = json.loads(checking_api_transfer.content)

    if not (validator.get("message") == "Autorizado"):
      return ExceptionsFactory.ExceptionReturn("transferir", "dinheiro, transferencia negada!", 403)

    beneficiario.saldo += quantidade
    remetente.saldo -= quantidade
    session.commit()

    return SuccessFactory.SuccessReturn("transferir", "dinheiro", 201)

  def __check_saldo_remetente(remetente, quantidade : float) -> bool:
    return False if remetente.saldo < quantidade else True