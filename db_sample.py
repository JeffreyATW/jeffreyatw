DEBUG = True

DATABASE_ENGINE = 'mysql'      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'jeffreyatw'   # Or path to database file if using sqlite3.
DATABASE_USER = 'jeffreyatw'   # Not used with sqlite3.
DATABASE_PASSWORD = '12345'    # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

MEDIA_ROOT = '/home/jeffreyatw/public_html/static/'

MEDIA_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

SECRET_KEY = '12345'

TEMPLATE_DIRS = (
    '/home/jeffreyatw/django/jeffreyatw/templates/'
)

RECAPTCHA_PUBLIC = '12345'
RECAPTCHA_PRIVATE = '12345'
