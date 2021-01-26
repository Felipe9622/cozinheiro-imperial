# cozinheiro-imperial


### Instalação para ambiente de desenvolvimento
Requer [Python](https://python.org/) instalado para rodar.
Clone o projeto.
Instale o Pipenv.
```sh
$ pip install pipenv
```
Instale as dependências com o Pipenv.
```sh
$ pipenv install
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
Abra o navegador com o endereço informado no console. A página de sucesso de instalação do Django deverá aparecer.

### Bibliotecas e framework utilizados

[django](https://www.djangoproject.com/) - Framework web desenvolvido em Python.

[gunicorn](https://gunicorn.org/) - Usa o WSGI para servir a aplicação Django.

[whitenoise](http://whitenoise.evans.io/en/stable/index.html) - Serve os arquivos estáticos sem a necessidade de um servidor externo, mantém contido na própria aplicação. 


