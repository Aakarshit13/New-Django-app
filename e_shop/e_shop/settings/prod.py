from .common import *
from os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NAME'),
        'HOST': os.getenv('HOST'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD')
    }
}

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ["3.108.54.77"]