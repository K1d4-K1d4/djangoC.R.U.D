## Projeto API de Livros com Django REST
Este projeto é uma API desenvolvida com Django REST Framework que permite cadastrar livros a partir da API do Google Books, consultar livros por título e armazenar informações como nota e resenha.

## Funcionalidades
- Consulta de livros por título usando a API do Google Books

- Cadastro automático com dados enriquecidos (autor, capa, título)

- Adição de nota e resenha personalizada

- Evita duplicatas com base no google_books_id

- API RESTful com suporte a GET, POST, PUT, DELETE

## Tecnologias utilizadas
Python 3.11+

Django 4+

Django REST Framework

Requests (para integração com Google Books API)


## Visão Geral
- Estrutura padrão de projetos Django.
- Suporte a APIs RESTful com Django REST Framework.
- Ambiente virtual localizado em `venv/` (não versionado).
- Dependências principais: `django`, `djangorestframework`, `requests`.

## Instalação e uso da aplicação
1. Clone o repositório e acesse o diretório do projeto.
2. Crie e ative o ambiente virtual (Windows):
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
4. Aplicar migrações:
  ```powershell
  venv\Scripts\python.exe manage.py makemigrations
  venv\Scripts\python.exe manage.py migrate
  ```
5. Rodar o servidor de desenvolvimento:
  ```powershell
  venv\Scripts\python.exe manage.py runserver
  ```

> Documentação será atualizada de acordo com a evolução .
