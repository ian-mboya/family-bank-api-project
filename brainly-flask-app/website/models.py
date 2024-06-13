from . import db
from flask_sqlalchemy import SQLAlchemy


class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(150), unique=True)
    program_name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phone_number = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    national_id_number = db.Column(db.String(150))
    date_of_birth = db.Column(db.String(150))
    date_enrolled = db.Column(db.String(150))





class Courses(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(150), unique=True)
    description = db.Column(db.String(150))
    department = db.Column(db.String(150))

    
class Enrollments(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(150), unique=True)
    course_id = db.Column(db.String(100))
    enrollment_date = db.Column(db.String(150))
    attained_grade = db.Column(db.String(150)) 

class Payments(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(150), unique=True)
    student_name = db.Column(db.String(150))
    amount = db.Column(db.Numeric(10, 2))
    payment_date = db.Column(db.String(150))