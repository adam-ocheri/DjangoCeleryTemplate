
import logging
from celery import shared_task

logger = logging.getLogger("dekelify")

@shared_task(name="test__periodic_task", queue="myqueue")
def test__periodic_task():
    logger.debug("test_task() | TASK IS WORKING!!!!!!!! ach DJYAKAAAARRR |")