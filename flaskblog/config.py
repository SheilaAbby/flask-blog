""" politico-app configurations """

from os import environ


class Config(object):
    """
    main config class
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    APP_SETTINGS = environ.get('APP_SETTINGS')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = environ.get('EMAIL_USER')
    MAIL_PASSWORD = environ.get('EMAIL_PASS')


class DevelopmentConfig(Config):
    """
    configurations for development env
    """
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """
    Testing env configs
    """
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """
    configs for staging app
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Config settings for production
    """
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}



