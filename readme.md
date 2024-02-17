# Sistema de Tranferência

O objetivo da arquitetura limpa é isolar as classes de negocios de todo o restante do ambiente, isso promove uma arquitetura quase que independente de tecnologia e facilita a implementação de testes.

- Esse projeto foi contruído com base no desafio do [**PicPay**](https://github.com/PicPay/picpay-desafio-backend)


## Setup da aplicação

- > Clone o repositório
- > Edite as variáveis de conexão com o banco de dados e certifique-se que ele existe. 
- > Na raiz do projeto rode o comando : `python3 initialize.py` para fazer o setup das tabelas.
- > Por fim basta executar a aplicação com o `python3 run.py` para iniciar a aplicação.

## Estrututra de Pastas

```bash
  ├── app
  │   ├── Adapter
  │   ├── Controller
  │   ├── Domain
  │   │   ├── Transferencia
  │   │   └── Usuarios
  │   ├── ReturnClass
  │   └── Services
  └── venv

```
