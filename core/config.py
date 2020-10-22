import os
import logging
import urllib
import socket

basedir = os.path.abspath(os.path.dirname(__file__))
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    LOG_LEVEL = os.environ.get('LOG_LEVEL', logging.INFO)

    VERSION = os.environ.get('VERSION', 'v0.4')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DC1_MSSQL = os.environ.get('DC1_MSSQL')
    DC2_MSSQL = os.environ.get('DC2_MSSQL')
    DC1_PREFIX = os.environ.get('DC1_PREFIX')
    DC2_PREFIX = os.environ.get('DC2_PREFIX')
    IP_DEFAULT_GW = os.environ.get('IP_DEFAULT_GW', ip_address)

    if IP_DEFAULT_GW[:8] == DC1_PREFIX:
        print('app running in DC1')
        MSSQL_HOST = DC1_MSSQL
    elif IP_DEFAULT_GW[:8] == DC2_PREFIX:
        print('app running in DC2')
        MSSQL_HOST = DC2_MSSQL
    else:
        MSSQL_HOST = os.environ.get('MSSQL_HOST')

    MSSQL_PORT = os.environ.get('MSSQL_PORT', '1433')
    MSSQL_USER = os.environ.get('MSSQL_USER', 'sa')
    MSSQL_PASS = os.environ.get('MSSQL_PASS', '')
    MSSQL_DB = os.environ.get('MSSQL_DB', 'cards')
    mssql_params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};' +
                                           f'SERVER={MSSQL_HOST};DATABASE={MSSQL_DB};UID={MSSQL_USER};PWD={MSSQL_PASS}')
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s' % mssql_params

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