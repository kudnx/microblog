import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-ultra-hyper-mega-viper-sercreta'