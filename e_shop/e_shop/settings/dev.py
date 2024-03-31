from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sys',
        'HOST': 'awsdj.cjo8gewom1q0.ap-south-1.rds.amazonaws.com',
        'USER': 'admin',
        'PASSWORD': 'heatedCar13'
    }
}