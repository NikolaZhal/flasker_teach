import datetime

import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

SqlAlchemyBase = orm.declarative_base()

__factory = None


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)

    def __repr__(self):
        return f' <Colonist> {self.id} {self.surname} {self.name}'


class Jobs(SqlAlchemyBase):
    __tablename__ = 'Jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    def __repr__(self):
        return f'<Job> {self.name} {self.email}'


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'

    engine = sqlalchemy.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)


def create_session() -> Session:
    global __factory
    return __factory()


def main(db_file):
    global_init(db_file)
    db_sess = create_session()
    data = max(db_sess.query(Jobs).filter(), key=lambda i: len(i.collaborators.split(', ')))
    equ = len(data.collaborators.split(', '))
    answer = []
    for job in db_sess.query(Jobs).all():
        if len(job.collaborators.split(', ')) == equ:
            user = db_sess.query(User).filter(User.id == job.team_leader).first()
            ans = f'{user.name} {user.surname}'
            if ans not in answer:
                answer.append(f'{user.name} {user.surname}')
    db_sess.commit()
    [print(i) for i in answer]


main(input())
