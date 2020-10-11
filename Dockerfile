FROM python:3-onbuild

# set a directory for the app
WORKDIR /usr/src/app

# set environment variables

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .