import os

API_TOKEN = os.environ['SLACK_TOKEN']

PLUGINS = [
#    'mumdico',
    'mumdico_auto'
]

BOT_EMOJI = ':face_with_monocle:'
ERRORS_TO = 'testbot'