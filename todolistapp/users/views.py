from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from todolistapp import db
from todolistapp.models import User, Todo
from todolistapp.users.forms import RegistrationForm, LoginForm
from todolistapp.todoposts.forms import AddJob
from wtforms import ValidationError
users = Blueprint('users', __name__)


@users.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/', methods = ['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Log In success!')
            return redirect(url_for('users.user_jobs', username = user.username))
        else:
            flash("Wrong Email or Password")
    return render_template('login.html', form=form)

@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))

@users.route("/<username>", methods = ['GET', 'POST'])
@login_required
def user_jobs(username):
    form  = AddJob()
    user = User.query.filter_by(username=username).first()
    if form.validate_on_submit():
        job = Todo(user_id=current_user.id, todotext=form.text.data)
        db.session.add(job)
        db.session.commit()
        form.text.data = ''
    jobs = Todo.query.filter_by(user_id=current_user.id)
    return render_template('user_jobs.html', jobs=jobs, form = form)

@users.route("/<int:job_id>/delete")
@login_required
def delete_job(job_id):
    job = Todo.query.get(job_id)
    db.session.delete(job)
    db.session.commit()
    flash('Job deleted')
    user = User.query.filter_by(id=current_user.id).first()
    return redirect(url_for('users.user_jobs', username=user.username))

@users.route("/<int:job_id>/job_status")
@login_required
def job_status(job_id):
    job = Todo.query.get(job_id)
    if job.completed:
        job.completed=False
    else:
        job.completed=True
    db.session.commit()
    flash('Job status updated')
    user = User.query.filter_by(id=current_user.id).first()
    return redirect(url_for('users.user_jobs', username=user.username))
