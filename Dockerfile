FROM python:3.11.4 as base

RUN mkdir /app

# set work directory
WORKDIR /app
# copy app contents
COPY . /app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate
# # # # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# # # # #
FROM base as mainapp
CMD daphne -b 0.0.0.0 -p 8000 main.asgi:application
# # # # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# # # # #
FROM base as celery_worker
CMD celery -A main worker -Q myqueue --loglevel=debug --pool=solo 
# # # # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# # # # #
FROM base as celery_beat
CMD celery -A main beat --loglevel=debug --scheduler django_celery_beat.schedulers:DatabaseScheduler
# # # # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# # # # #
FROM base as flower
CMD celery flower -A main --port=5555
# # # # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
