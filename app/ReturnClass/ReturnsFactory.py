class ExceptionsFactory:
    """
        Classe para retornar os erros ocorridos em runtime.
    """

    @classmethod
    def ExceptionReturn(cls, verbo: str, objeto: str, stts_code = 400):
        return {"message": f"Não foi possível {verbo} o {objeto}", "error": True}, stts_code


class SuccessFactory:
    """
        Classe para retornar o sucessos obtidos em runtime
    """

    @classmethod
    def SuccessReturn(cls, verbo: str, subs: str, stts_code = 200):
        return {"message": f"Com sucesso foi {verbo} o {subs}!", "error": False}, stts_code
