from base import *

DEBUG = False
ALLOWED_HOSTS = ['54.193.56.228']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # To create one in MySQL: CREATE DATABASE sitedb CHARACTER SET utf8 COLLATE utf8_unicode_ci;
        'NAME': 'hobbout',                    # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'yitingvvv',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}


AWS_ACCESS_KEY_ID = 'AKIAIS4JPQBNHQAHBWIA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_SECURE_URLS = False

AWS_S3_CUSTOM_DOMAIN = 'dr7777o8hif8c.cloudfront.net'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 's3.hobbout.com'

AWS_HEADERS = {
    'Cache-Control': 'max-age=31536000',
}

AWS_STATIC_HEADERS = {
    'Cache-Control': 'max-age=2592000',
}


AWS_STATIC_S3_CUSTOM_DOMAIN = 'dhnbhn87vf578.cloudfront.net'
AWS_STATIC_STORAGE_BUCKET_NAME = 'assets.hobbout.com'
AWS_STATIC_PATH = 'assets'

AWS_PRELOAD_METADATA = True

STATIC_URL = 'http://%s/%s/' % (AWS_STATIC_S3_CUSTOM_DOMAIN, AWS_STATIC_PATH)
DEFAULT_AVATAR_LOCATION = STATIC_URL + 'img/avatar/'

STATICFILES_STORAGE = 'core.s3storage.S3PipelineStorage'

MEDIA_URL = 'http://%s/' % (AWS_S3_CUSTOM_DOMAIN)
IMAGE_PATH_PREFIX = 'media/images/origin'
FILE_PATH_PREFIX = 'media/files/origin'
VIDEO_PATH_PREFIX = 'media/videos/origin'

"""
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ' memcached.oki6tj.cfg.usw1.cache.amazonaws.com:11211',
        'MAX_ENTRIES': 10000,
    }
}
"""


if DEBUG:

    THUMBNAIL_DEBUG = True

    INTERNAL_IPS = ('127.0.0.1')

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        #'debug_toolbar.panels.profiling.ProfilingDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
