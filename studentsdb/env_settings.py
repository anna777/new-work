import os

from .local import DB_USER, DB_PASSWORD
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'manin@%*of)orvk!t_^9_#&snqxvhyh9i&4dnfiz_jv4w0(o-6'
ALLOWED_HOSTS = ['students.annapasichnyk.com',
'demo-students.vitaliypodoba.com']
DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'HOST':'localhost',
        'USER': DB_USER,
        'PASSWORD':DB_PASSWORD,
        'NAME': 'students_db',

    }
}
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'students.annapasichnyk.com']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
# admins
ADMINS = (('Anna', 'annapasichnyk77@gmail.com'),)
MANAGERS = (('Manager', 'annapasichnyk77@gmail.com'),)
