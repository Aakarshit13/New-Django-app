import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_shop.settings.prod')

celery = Celery('e_shop')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()