# Site de Receitas

## Descrição

Neste exercício, criei uma aplicação em Python utilizando o framework Django.

Foi desenvolvido um site de receitas e também aprendi as boas práticas seguindo as principais convenções do Django, refatorando o template evitando os código duplicado com partials e estendendo o código html.

Além disso, conectei a aplicação com o banco de dados Postgres e utilizei o admin do Django para criar, editar e deletar receitas (CRUD), exibindo as receitas de forma dinâmica.

## Ferramentas usadas
1. [Python 3.10](https://docs.python.org/3/)
2. [Django 4](https://docs.djangoproject.com/pt-br/4.0/)
3. [PostgreSQL](https://www.postgresql.org/)

## Como rodar
Para testar, execute o virtualenv com às dependências do projeto. Execute o servidor django, executando na pasta `Site_de_Receitas` o comando `python manage.py runserver`.

Acesse `http://localhost:8000/`. Ao fim, você será direcionado a página inicial.

Para acessar a pagina admin, basta acessar `http://localhost:8000/admin`. Para criar um novo usuário basta abrir outro terminal na venv e digitar `python manage.py createsuperuser`.
