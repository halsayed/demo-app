import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    LOG_LEVEL = os.environ.get('LOG_LEVEL', logging.INFO)

    VERSION = os.environ.get('VERSION', 'v1.0')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///tmp.db')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class UatConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig(),
    'testing': TestConfig(),
    'production': ProductionConfig(),
    'uat': UatConfig(),

    'default': DevelopmentConfig()
}


# create logger
log = logging.getLogger()
log.setLevel(Config.LOG_LEVEL)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(Config.LOG_LEVEL)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
log.addHandler(ch)