import os
from mineralsearch.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = [
    '.herokuapp.com',
    'localhost',
    ]
SECRET_KEY = get_env_variable('SECRET_KEY')