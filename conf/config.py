
class Config:

    APP_NAME = "http-to-zabbix-sender"
    AUTHOR = "Fabio Azevedo"
    AUTHOR_EMAIL = "emaildofabioeduardo@gmail.com"


class DevConfig(Config):
    DEBUG = True
    APP_PORT = 8080


class ProdConfig(Config):
    DEBUG = False
    APP_PORT = 80
