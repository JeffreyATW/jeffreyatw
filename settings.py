import db

# Django settings for jeffreyatw project.

DEBUG = db.DEBUG
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = db.DATABASE_ENGINE
DATABASE_NAME = db.DATABASE_NAME
DATABASE_USER = db.DATABASE_USER
DATABASE_PASSWORD = db.DATABASE_PASSWORD
DATABASE_HOST = db.DATABASE_HOST
DATABASE_PORT = db.DATABASE_PORT

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = db.TIME_ZONE

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = db.LANGUAGE_CODE

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = db.MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = db.MEDIA_URL

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = db.ADMIN_MEDIA_PREFIX

# Make this unique, and don't share it with anybody.
SECRET_KEY = db.SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
 'django.middleware.common.CommonMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'jeffreyatw.urls'

TEMPLATE_DIRS = db.TEMPLATE_DIRS

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'jeffreyatw.car',
    'jeffreyatw.portfolio',
    'jeffreyatw.lasers',
    'jeffreyatw.landing',
    'jeffreyatw.binaryimage',
)

RECAPTCHA_PUBLIC = db.RECAPTCHA_PUBLIC
RECAPTCHA_PRIVATE = db.RECAPTCHA_PRIVATE
