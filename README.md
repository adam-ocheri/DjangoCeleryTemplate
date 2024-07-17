# Django Celery Template

## Prerequisites
- Python >= 3.11
- Docker and DockerCompose
- virtualenv

## Installation
1. Create a new python environment: `$ python -m venv env`
2. Initialize newly created environment
    - If using a bash terminal: `$ source env/Scripts/activate`
    - If using a command prompt: `$ env\Scripts\activate`
3. Install dependencies as listed in **requirements.txt**: `$ pip install .`

## Setup Django
1. Run **Django** migrations: `$ python manage.py makemigrations && python manage.py migrate` 
2. Log in with the pre-created Super User; name is `admin` and password is `admin` as well. Alternatively, you can create a new Super User to use the django admin: `$ python manage.py createsuperuser` (enter your name and password, email is not mandatory[press Enter to skip inserting email])
3. When you run django, you will be able to log into the django admin using your username and password, at `http://127.0.0.1:8000/admin/`

## Run
- Simply build the images and run the containers via `$ docker-compose up`

## Monitoring
- You can monitor the health of the DockerCompose stack by visiting `http://127.0.0.1:9090/` via prometheus
- You can modify the `alertmanager.yml` and follow the instructions to include a mail addresses to which alerts would get to (and be sent from)
- You can enter and see your Grafana boards at `127.0.0.1:3000`, with the default username `admin` and password `admin`