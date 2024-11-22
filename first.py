from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()#ініціалізація об'єкта для роботи з БД
bcrypt = Bcrypt()#ініціалізація бібліотеки для хешування паролів

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)#унікальний номер
    #ім'я користувача (обов'язкове та унікальне)
    username = db.Column(db.String(50), nullable = False, unique = True)
    #пошта користувача (обов'язкова та унікальна)
    email = db.Column(db.String(120), nullable = False, unique= True)
    #хеширований пароль
    password = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(10), nullable = False, default="student")

    #статичний метод для хешування паролів
    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    #метод для перевірки хешей пароля
    def check_password(self, password):
        #повертає 1 якщо хеш співпадає
        return bcrypt.check_password_hash(self.password, password)
