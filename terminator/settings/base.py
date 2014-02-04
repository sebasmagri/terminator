# -*- coding: utf-8 -*-
#
# Copyright 2011, 2013 Leandro Regueiro
#
# This file is part of Terminator.
# 
# Terminator is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# 
# Terminator is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# Terminator. If not, see <http://www.gnu.org/licenses/>.

import sys

from funfactory.settings_base import *  # NOQA

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

LANGUAGES = ('en', 'es', 'gl', 'pt')

LOCALE_PATHS = (
    os.path.join(os.path.dirname(__file__), 'locale').replace('\\', '/'),
)


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
    'guardian.backends.ObjectPermissionBackend',
)

ANONYMOUS_USER_ID = -1

INSTALLED_APPS = get_apps(
    exclude=('cronjobs', 'djcelery', 'django_browserid', 'product_details'),
    append=('django.contrib.admin', 'django.contrib.comments',
            'django.contrib.sites', 'guardian', 'registration', 'profiles',
            'terminator.terminator', 'terminator.terminator_comments_app')
)

MIDDLEWARE_CLASSES = get_middleware()

TEMPLATE_CONTEXT_PROCESSORS = get_template_context_processors()

JINGO_EXCLUDE_APPS = ('admin', 'registration', 'profiles',
                      'context_processors', 'terminator',
                      'terminator_comments_app')

AUTH_PROFILE_MODULE = "terminator.UserProfile"

# One-week activation window; you may, of course, use a different value.
ACCOUNT_ACTIVATION_DAYS = 7

COMMENTS_APP = 'terminator.terminator_comments_app'

EMAIL_PORT = 1025

SEND_NOTIFICATION_EMAILS = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
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
            'filters': ['require_debug_false', ],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'stdout': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'strm': sys.stdout
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['stdout', ],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}
