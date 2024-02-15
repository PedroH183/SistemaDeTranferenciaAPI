from run import engine, Base
from app.Domain.UsuariosComumModel import UsuarioComum
from app.Domain.UsuariosLojistaModel import Lojista

def init_db():
    """
      Função responsável por criar todas as tabelas no banco de dados.
    """

    # delete all tables
    Base.metadata.drop_all(bind=engine)

    # create all tables
    Base.metadata.create_all(bind=engine)

    print("Initialized the db")


if __name__ == "__main__":
    init_db()
