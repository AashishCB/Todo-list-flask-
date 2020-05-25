from todolistapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader # responsible for fetching the current_user
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    todo = db.relationship('Todo',backref='users',lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"


class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    dateandtime = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    completed = db.Column(db.Boolean(), nullable=False, default = False)
    todotext = db.Column(db.Text,nullable=False)

    def __init__(self, user_id, todotext):
        self.user_id = user_id
        self.todotext = todotext


    def __repr__(self):
        return f"{self.todotext}"
