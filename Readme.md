# Django-stripe

Тестовое задание - Django-сервер с использованием Stripe API

### Installation

- Make sure port 8888 is free
- Install [Docker](https://www.docker.com/)

- Run Docker image from repository

```sh
$ sudo docker run -p 8888:8080 --name MyContainer lerese58/django-stripe
```

For using admin page you have to create superuser:
```sh
$ sudo docker exec -it MyContainer python3 manage.py createsuperuser
```
