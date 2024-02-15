# Arquitetura Limpa Ou Arquitetura Hexagonal

O objetivo da arquitetura hexagonal é isolar as classes de negocios de todo o restante do ambiente, isso promove uma arquitetura quase que independente de tecnologia e facilita a implementação de testes.

`Esse projeto foi contruído com base no desafio [https://github.com/PicPay/picpay-desafio-backend] do PicPay`

## Como fazer o setup das tabelas
É ligeiramente complicado fazer o setup das tabelas sem o uso das migrates então deixei detalhado abaixo o procedimento.

- > Clone o repositório
- > Edite as variáveis de conexão com o banco de dados 
- > Rode o comando : `export FLASK_RUN=run & Flask shell `
- > No terminal do projeto rode `from run import db, Filho, Genitor`
- > Rode após `db.create_all()` e saia do terminal
- > Por fim basta executar a aplicação com o `python3 run.py`

## Estrututra de Pastas

```bash
  .
  ├── app
  │   ├── Adapter
  │   ├── Controller
  │   ├── Domain
  │   └── Model
  └─- venv

```

- > Adapter == código responsável por se comunicar com Domain.
- > Controller== código responsável por tratar as requisições.
- > Domain == código referente as regras de negócio do sistema.
- > Model == código responsável por representar as entidades do sistema.