from .base import *  # noqa: F403
from decouple import config

SILENCED_SYSTEM_CHECKS = [
    # security.W005, SECURE_HSTS_PRELOAD
    # We are not ready to submit the site to the HSTS preload list,
    # as it is in development
    "security.W021",
]

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET")

SECURE_HSTS_SECONDS = 60  # Set to 1 minute while prototyping
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")]
)
