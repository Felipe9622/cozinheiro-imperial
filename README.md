# cozinheiro-imperial
[![Build Status](https://travis-ci.org/django-ferrata/cozinheiro-imperial.svg?branch=main)](https://travis-ci.org/django-ferrata/cozinheiro-imperial) 

### Instalação para ambiente de desenvolvimento
Requer [Python](https://python.org/) instalado para rodar.
Clone o projeto.
Instale o Pipenv.
```sh
$ pip install pipenv
```
Instale as dependências de desenvolvimento com o Pipenv.
```sh
$ pipenv sync -d
```
Inicie o ambiente virtual.
```sh
$ pipenv shell
```
Aplica as migrações. 
```sh
$ python manage.py makemigrations 
```
Teste subindo o servidor de desenvolvimento.
```sh
$ python manage.py runserver
```
Abra o navegador com o endereço informado no console. O app devera abrir 

### Bibliotecas e framework utilizados

[django](https://www.djangoproject.com/) - Framework web desenvolvido em Python.

[gunicorn](https://gunicorn.org/) - Usa o WSGI para servir a aplicação Django.

[whitenoise](http://whitenoise.evans.io/en/stable/index.html) - Serve os arquivos estáticos sem a necessidade de um servidor externo, mantém contido na própria aplicação. 

[flake8](https://flake8.pycqa.org/en/latest/manpage.html) - Usado para fazer o lint do codigo.

[travis-ci](https://travis-ci.org/) - Usado para integraçao continua

[python-decouple]()

[psycopg2-binary]()

[dj-database-url](https://github.com/jacobian/dj-database-url)