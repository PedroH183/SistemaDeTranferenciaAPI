class ExceptionsFactory:
    """
        Classe para retornar os erros ocorridos em runtime.
    """

    @classmethod
    def ExceptionReturn(cls, verbo: str, subs: str):
        return {"message": f"Não foi possível {verbo} o {subs}", "error": True}, 404


class SuccessFactory:
    """
        Classe para retornar o sucessos obtidos em runtime
    """

    @classmethod
    def SuccessReturn(cls, verbo: str, subs: str):
        return {"message": f"Com sucesso foi {verbo} o {subs}!", "error": False}, 200
