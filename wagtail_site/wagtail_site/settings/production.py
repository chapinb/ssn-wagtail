from .base import *  # noqa: F403
from decouple import config

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET")
