# Sistema de Transferência

- Esse projeto foi contruído com base no desafio do [**PicPay**](https://github.com/PicPay/picpay-desafio-backend)


## Setup da aplicação

- > Clone o repositório
- > Edite as variáveis de conexão com o banco de dados no arquivo `settings.py` e certifique-se que ele existe. 
- > Na raiz do projeto rode o comando `docker compose up` esse comando criará todo o ambiente necessário para a aplicação e após a aplicação estará rodando.

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
  │── settings.py
  │── run.py
  └── venv
```

## Api Endpoints

A Api dispõem dos seguintes endpoints : 

### Api Usuario Comum
```
  POST   /usuario/add - Create a new commom user
  GET    /usuario/all - Retrieve all commoms users
  GET    /usuario/view/{id} - Updates a commom user
  DELETE /usuario/delete/{id} - Delete a commom user
  POST   /usuario/transferirDinheiro - transferir 
```
### Body 
```bash
  ## data body of a commom user
{
  "saldo" : 123
  "senha" : "123",
  "cpf" : "111.114.574-25",
  "email" : "pedro@gmail.com",
  "nome_completo" : "Pedro Henrique",
}
```
### Api Lojista
```bash
  POST   /lojista/add - Create a new shopkeeper
  GET    /lojista/all - Retrieve all shopkeepers
  GET    /lojista/view/{id} - Updates a shopkeeper
  DELETE /lojista/delete/{id} - Delete a shopkeeper
```
### Body
```bash
{
  "saldo" : 123,
  "senha" : "1234",
  "nome_completo" : "Pedro Henrique",
  "cnpj" : "31.231.231/2001-99",
  "email" : "pedro@email.com"
}
```


