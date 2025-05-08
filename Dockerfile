FROM python:3.12

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

ENV APP_HOME=/usr/src/app
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/media

COPY . /usr/src/app/

ENTRYPOINT ["bash", "/usr/src/app/entrypoint.sh"]
