# djangoC.R.U.D

Projeto base para construção de aplicações CRUD utilizando Django e Django REST Framework.

## Visão Geral
- Estrutura padrão de projetos Django.
- Suporte a APIs RESTful com Django REST Framework.
- Ambiente virtual localizado em `venv/` (não versionado).
- Dependências principais: `django`, `djangorestframework`, `requests`.

## Instalação
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

## Comandos Essenciais
- Criar novo app:
  ```powershell
  venv\Scripts\python.exe manage.py startapp <nome_do_app>
  ```
- Aplicar migrações:
  ```powershell
  venv\Scripts\python.exe manage.py makemigrations
  venv\Scripts\python.exe manage.py migrate
  ```
- Rodar o servidor de desenvolvimento:
  ```powershell
  venv\Scripts\python.exe manage.py runserver
  ```
- Criar superusuário:
  ```powershell
  venv\Scripts\python.exe manage.py createsuperuser
  ```
- Executar testes:
  ```powershell
  venv\Scripts\python.exe manage.py test
  ```

> Documentação será atualizada de acordo com a evolução .
