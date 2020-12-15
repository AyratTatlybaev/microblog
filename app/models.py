from app import db

class User(db.Model):
    '''
    Класс User наследует от db.Model,
    базового класса для всех моделей из Flask-SQLAlchemy.
    Этот класс определяет несколько полей как переменные класса.
    Поля создаются как экземпляры класса db.Column,
    который принимает тип поля в качестве аргумента,
    плюс другие необязательные аргументы, которые, например,
    позволяют мне указать, какие поля уникальны и индексированы,
    что важно для эффективного поиска базы данных.

    Метод __repr__ сообщает Python, как печатать объекты этого класса,
    что будет полезно для отладки.
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.Datetime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
