FROM python:3.11.4 as base

# RUN apt-get update 
# && \
#     apt-get install -y ffmpeg python3-pyaudio portaudio19-dev 

RUN mkdir /app

# set work directory
WORKDIR /app

COPY . /app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
# COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# copy project

# RUN pip install .
# RUN python setup.py install
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
