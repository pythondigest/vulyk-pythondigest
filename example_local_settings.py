# -*- coding: utf-8 -*-


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

# This one only works to log in via http://localhost:5000
SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

# This one only works to log in via http://localhost:5000
SOCIAL_AUTH_VK_OAUTH2_KEY = ''
SOCIAL_AUTH_VK_OAUTH2_SECRET = ''

SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''


MONGODB_SETTINGS = {
    'DB': "database_name",
}

ENABLED_TASKS = {
    'vulyk_pythondigest_moderator': 'PythonDigestModeratorTaskType',
}

TEMPLATE_BASE_FOLDERS = [
    'pythondigest_moderator_task',
]

WARM_WELCOME = u"""
<h3>Вас приветствует проект <br><a href="https://pythondigest.ru">Python Дайджест</a></h3>
"""

LANGUAGE = 'ru'
SITE_NAME = u'Python Дайджест'
SITE_MOTTO = u'Python Дайджест'
SITE_LOGO = 'https://pythondigest.ru/static/img/logo.png'
