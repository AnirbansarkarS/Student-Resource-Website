from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # hashed password

    def __repr__(self):
        return f"<User {self.name}>"

# Course Table
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # B.Tech, BBA, BCA, etc.
    university = db.Column(db.String(100), nullable=False, default="Techno India University")
    year = db.Column(db.Integer, nullable=False)  # Year number: 1,2,3,4
    semester = db.Column(db.Integer, nullable=False)  # Semester: 1 or 2

    resources = db.relationship('Resource', backref='course', lazy=True)

    def __repr__(self):
        return f"<Course {self.name} Year {self.year} Sem {self.semester}>"

# Resource Table
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)  # Example: "B.Tech 1st Sem Syllabus"
    type = db.Column(db.String(50), nullable=False)   # syllabus, notes, playlist, PYQs
    link = db.Column(db.String(500), nullable=False)  # PDF link or playlist link
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __repr__(self):
        return f"<Resource {self.title} ({self.type})>"
