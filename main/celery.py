import os
from celery import Celery
import logging

logger = logging.getLogger("dekelify")


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main',)#, broker_transport_options={"heartbeat": 0})
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):

    logger.debug(f'Django Celery task debug Request: {self.request!r}')