# Django-stripe

Тестовое задание - Django-сервер с использованием Stripe API

  - Type some Markdown on the left
  - See HTML in the right
  - Magic

### Installation

0) Make sure port 8888 is free
1) Install [Docker](https://www.docker.com/)

After that, run Docker image from repository

```sh
$ sudo docker run -p 8888:8080 --name MyContainer lerese58/django-stripe
```

For using admin page you have to create superuser:
```sh
$ sudo docker exec -it MyContainer python3 manage.py createsuperuser
```
