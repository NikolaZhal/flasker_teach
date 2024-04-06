import os

from flask import Flask
from flask import render_template, request
from flask import session

from data import db_session
from data.jobs import Jobs
from data.users import User
from data.department import Department
from forms.user import RegisterForm, TwoLogin

UPLOAD_FOLDER = './static/img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

planet_data = {
    'марс': ['Эта планета близка к Земле;', 'На ней много необходимых ресурсов;', 'На ней есть вода и атмосфера;',
             'На ней есть небольшое магнитное поле;', 'Наконец, она просто красива!']
    , 'непун': ['Нептун как Нептун;', '8 планета от солнца;', 'Наконец, она просто красива!']
    , 'юпитер': ['Юпитер как Юпитер', '5 планета от солнца;', 'Наконец, она просто красива!']
    , 'земля': ['Земля наш дом', '3 планета от солнца;', 'Наконец, она просто красива!']
    , 'меркурий': ['Меркурий как Меркурий', '1 планета от солнца;', 'Наконец, она просто красива!']
    , 'венера': ['Венера как Венера', '2 планета от солнца;', 'Наконец, она просто красива!']
    , 'сатурн': ['Сатурн как Сатурн', '6 планета от солнца;', 'Наконец, она просто красива!']
    ,
    'уран': ['Уран как Уран', '7 планета от солнца;', 'Наконец, она просто красива!']
}
profs = ['инженер-исследователь', 'пилот', 'строитель',
         'экзобиолог', 'врач', 'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
         'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
         'киберинженер', 'штурман', 'пилот дронов']


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    for user in db_sess.query(User).filter(User.address == 1):
        print(user)

    db_sess.commit()

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    # db_sess = db_session.create_session()
    # db_sess.commit()    
    # user = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title="Личная запись", content="Эта запись личная", 
    #             is_private=True)


#     # user.news.append(news)

@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    for i in jobs:
        during = i.end_date - i.start_date
        i.add_during(during.total_seconds() / 3600)
    names = ['Название работы', 'фамилия и имя ответственного', 'продолжительность в часах', 'список id команды',
             'завершена или нет']
    turn = ['job', 'team_leader', 'during', 'collaborators', 'is_finished']
    gg = ['id', 'job', 'work_size', 'is_finished', 'start_date', 'end_date', 'team_leader', 'collaborators']
    return render_template("index.html", jobs=jobs, names=names, turn=turn)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = {i.name: i.data for i in form}
            session['auto_answer'] = data
            return f'''<!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <title>Title</title>
                                </head>
                                <body>
                                {str(data)}
                                </body>
                                </html>'''
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def twologin():
    form = TwoLogin()
    return render_template("two_def.html", form=form)


def create_user(*data):
    """surname, name, age, position, speciality, address, email"""
    user = User()
    user.surname = data[0]
    user.name = data[1]
    user.age = data[2]
    user.position = data[3]
    user.speciality = data[4]
    user.address = data[5]
    user.email = data[6]
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


# def create_job():
#     jobs = Jobs()
#     jobs.team_leader = 1
#     jobs.job = 'deployment of residential modules 1 and 2'
#     jobs.work_size = 15
#     jobs.collaborators = '2, 3'
#     # jobs.start_date = '(now)'
#     jobs.is_finished = False
#     db_sess = db_session.create_session()
#     db_sess.add(jobs)
#     db_sess.commit()

if __name__ == '__main__':
    main()

# @app.route('/register', methods=['GET', 'POST'])
# def reqister():
#     form = RegisterForm()
#     print('lllllllllllllllllllllll')
#     print(form.knowlarge.data)
#     print(form.validate_on_submit())
#     print(form.errors)
#     if form.validate_on_submit():
#         print('aaaaaaaaaaa')
#         # if form.password.data != form.password_again.data:
#         #     return render_template('register.html', title='Регистрация',
#         #                            form=form,
#         #                            message="Пароли не совпадают")
#         # db_sess = db_session.create_session()
#         # print(form)
#         # if db_sess.query(User).filter(User.email == form.email.data).first():
#         #     return render_template('register.html', title='Регистрация',
#         #                            form=form,
#         #                            message="Такой пользователь уже есть")
#         # user = User(
#         #     name=form.name.data,
#         #     email=form.email.data,
#         #     about=form.about.data
#         # )
#         # user.set_password(form.password.data)
#         # db_sess.add(user)
#         # db_sess.commit()
#         return redirect(url_for(f'/answer', data=form))
#     return render_template('register.html', title='Регистрация', form=form)
