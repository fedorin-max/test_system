from email.policy import default

from flask import Flask, render_template, request, redirect, url_for,flash
#підтягуємо із файла first БД, клас користувача та хешування
from first import db, User, bcrypt

app  = Flask(__name__)#створили фласк-додаток
#налашутвання БД
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
#відключення відстежння змін (оптимізація)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#ключ для роботи з сессіями и флеш повідомленнями
app.config['SECRET_KEY']='password'

#ініціалізація БД та біббліотеки хешування
db.init_app(app)
bcrypt.init_app(app)

#автоматичне створення таблиць і БД, якщо вони не існують
with app.app_context():
    db.create_all()

#маршрут для сторінки реєстреції
@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':#якщо форму відправили
        #отримаємо дані із форми
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        #перевірка наявности імені у БД
        if User.query.filter_by(username = username).first():
            flash("Username already exists")
            return redirect(url_for('register'))
        #перевірка наявности пошти в БД
        if User.query.filter_by(email = email).first():
            flash("Email already exists")
            return redirect(url_for('register'))
        #якщо пошта та ім'я унікальні
        #свторюємо хеширований пароль
        hashed_password = User.hash_password(password)
        #створюємо екземпляр класа, куди передаємо наші дані
        new_user = User(username = username, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()#закриваємо сессію

        flash("Register complite")
        return redirect(url_for('register'))
    #якщо використали метод GET (користувач відкрив сторінку реєстрації)
    #повертаєс сторінку
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug= True)