from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
from datetime import datetime
from flask_login import LoginManager
from data.db_session import global_init, create_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


def create_users():
    db_sess = db_session.create_session()
    capitane = User()
    capitane.surname = 'Scott'
    capitane.name = 'Ridley'
    capitane.age = 21
    capitane.position = 'capitane'
    capitane.speciality = 'research engineer'
    capitane.address = 'module_1'
    capitane.email = 'scott_chief@mars.org'

    pilot = User()
    pilot.surname = 'Weir'
    pilot.name = 'Andy'
    pilot.age = 25
    pilot.position = 'pilot'
    pilot.speciality = 'pilot'
    pilot.address = 'module_2'
    pilot.email = 'weir@mars.org'

    builder = User()
    builder.surname = 'Watney'
    builder.name = 'Mark'
    builder.age = 22
    builder.position = 'builder'
    builder.speciality = 'builder'
    builder.address = 'module_3'
    builder.email = 'watney@mars.org'

    biolog = User()
    biolog.surname = 'Sanders'
    biolog.name = 'Taddy'
    biolog.age = 18
    biolog.position = 'biolog'
    biolog.speciality = 'biolog'
    biolog.address = 'module_4'
    biolog.email = 'sanders@mars.org'

    db_sess = db_session.create_session()
    db_sess.add(capitane)
    db_sess.add(pilot)
    db_sess.add(builder)
    db_sess.add(biolog)
    db_sess.commit()


def add_job():
    job = Jobs()
    job.team_leader = 1
    job.job = 'job deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.now()
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


def main():
    # db_session.global_init("db/mars_explorer.db")
    # add_job()
    global_init(input())
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == 'module_1',
                                           User.speciality.notilike("%engineer%"),
                                           User.position.notilike("%engineer%")):
        print(user.id)

    app.run()


if __name__ == '__main__':
    main()