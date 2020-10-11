FROM python:3-onbuild
EXPOSE 8000
CMD "python3 manage.py runserver"