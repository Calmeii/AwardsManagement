from . import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stu_no = db.Column(db.String(32), nullable=False, unique=True)
    name = db.Column(db.Unicode(128))
    department = db.Column(db.Unicode(128))
    major = db.Column(db.Unicode(128))
    grade = db.Column(db.String(32))

    def __repr__(self):
        return '<Student %s %s>' % (self.stu_no, self.name)