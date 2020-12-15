import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Расширение Flask-SQLAlchemy принимает местоположение базы данных
    # приложения из переменной конфигурации SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # Параметр конфигурации SQLALCHEMY_TRACK_MODIFICATIONS
    # установлен в значение False, чтобы отключить функцию
    # Flask-SQLAlchemy, которая мне не нужна, которая должна
    # сигнализировать приложению каждый раз, когда в базе данных
    # должно быть внесено изменение.
    SQLALCHEMY_TRACK_MODIFICATIONS = False