
import logging
from celery import shared_task

logger = logging.getLogger("dekelify")

@shared_task(name="test_task", queue="myqueue")
def test_task():
    logger.debug("test_task() | TASK IS WORKING!!!!!!!! ach DJYAKAAAARRR |")