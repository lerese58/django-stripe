FROM python:3-onbuild

# install dependencies
EXPOSE 8080

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

#docker run -p 8000:8080 lerese58/django-stripe