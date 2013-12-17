# Django settings for hobbout project.
from unipath import Path

PROJECT_DIR = Path(__file__).ancestor(3)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Yiting Li', 'yl2919@columbia.edu'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR.child('media')

IMAGE_PATH_PREFIX = 'images/origin'
THUMBNAIL_PATH_PREFIX = 'thumbnails'
THUMBNAIL_BACKEND = 'mediabox.backends.CustomThumbnailBackend'
# THUMBNAIL_UPSCALE = False

FILE_PATH_PREFIX = 'files/origin'
VIDEO_PATH_PREFIX = 'videos/origin'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://127.0.0.1:8000/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_DIR.child('assets')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

DEFAULT_AVATAR_LOCATION = STATIC_URL + 'img/avatar/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR.child('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

DJANGO_WYSIWYG_FLAVOR = "ckeditor"
DJANGO_WYSIWYG_MEDIA_URL = STATIC_URL + 'ckeditor/'
CKEDITOR_UPLOAD_PATH = PROJECT_DIR # Must block the upload functionality

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
}

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_JS = {
    'libs': {
        'source_filenames': (
            'js/libs/jquery-1.10.2.js',
            'js/libs/jquery.cookie.js',
            'js/libs/bootstrap.js',
            'js/crfs.js',
        ),
        'output_filename': 'js/libs.js',
    },

    'topic': {
        'source_filenames': (
            'js/topic.js',
        ),
        'output_filename': 'js/topic.js',
    },

}

PIPELINE_CSS = {
    'libs': {
        'source_filenames': (
            'css/bootstrap.css',
            #'css/ui/jquery-ui-1.10.3.custom.css',
        ),
        'output_filename': 'css/libs.css',
    },

    'global': {
        'source_filenames': (
            'css/main.css',
        ),
        'output_filename': 'css/global.css',
    },

    'ckeditor_custom': {
        'source_filenames': (
            'css/ckeditor_custom.css',
        ),
        'output_filename': 'css/ckeditor_custom.css',
    }
}


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'um@+c4qsmja90f)mfb%q6dl++o@bpxje-8vbry88=!-+k)l(s@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    # project context processors
    'core.context_processors.template_constants',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hobbout.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'hobbout.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR.child('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',

    # 3rd party apps,
    'django_wysiwyg',
    'tinymce',
    'pipeline',
    'rest_framework',
    'rest_framework.authtoken',
    'social_auth',
    'sorl.thumbnail',
    'south',
    'widget_tweaks',

    # My apps
    'activities',
    'ckeditor',
    'groups',
    'locations',
    'mediabox',
    'mediaframes',
    'topics',
    'users',
)

# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTH_USER_MODEL = 'users.TingUser'

AUTHENTICATION_BACKENDS = (
    'users.backends.weibo.WeiboBackend',
    #'social_auth.backends.contrib.weibo.WeiboBackend',
    'users.backends.auth.EmailOrUsernameModelBackend',
    #'django.contrib.auth.backends.ModelBackend'
)

PAGE_SIZE = {
    'MICROBLOG': 10,
    'MICROCOMMENT': 5,
    'NOTEBOARD': 10,
    'NOTE': 50,
    'BLOG': 10,
    'ALBUM': 15,
    'MEDIAFRAME': 30,

    'POPULAR_SIDEBAR': 6,
}

IMAGE_SIZE = {

    'AVATAR_XTINY': '23',
    'AVATAR_TINY': '50',
    'AVATAR_SMALL': '96',
    'AVATAR_XTINY_CROPPED': '20x20',
    'AVATAR_TINY_CROPPED': '50x50',
    'AVATAR_SMALL_CROPPED': '96x96',

    'MICROBLOG_IMAGE': '533x400',

    'FRAME_LIST_CROPPED': '282x188',
    'FRAME_DETAIL': '822x690',

    'ALBUM_COVER_CROPPED': '212x150',
    'ALBUM_COVER_WIDTH': '212',
    'ALBUM_COVER_HEIGHT': '150',
    'FRAME_THUMB_CROPPED': '50x50',
    'FRAME_THUMB_WIDTH': '50',

    'POPULAR_SIDEBAR': '130',
}

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/register/'
LOGIN_ERROR_URL = '/login-error/'

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        #'rest_framework.authentication.OAuth2Authentication',
    ),

    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ),

    'PAGINATE_BY': 10
}

UPLOAD_VIDEO_TYPES = ['video/mp4']
