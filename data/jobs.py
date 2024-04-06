import datetime

import sqlalchemy
import sqlalchemy.orm as orm

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'Jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    user = orm.relationship('User')

    def __repr__(self):
        return f'<Job> {self.id} {self.job}'

    def add_during(self, data):
        self.during = data
