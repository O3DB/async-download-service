import os


basedir = os.path.abspath(os.path.dirname(__file__))


class CONFIG:
    SERVICE_NAME = 'MarriageAgency'
    SERVICE_PORT = int(os.environ.get('SERVICE_PORT', 8080))
    MEDIA_URI = os.path.join(basedir, os.getenv('PHOTOS_PATH', 'static/test_photos'))
    TEMPLATES_URI = os.path.join(basedir, 'templates')
    DELAY = int(os.getenv('DELAY', 0))
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
