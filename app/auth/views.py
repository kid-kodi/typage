# app/home/views.py

from flask_login import current_user, login_user, logout_user

from werkzeug.urls import url_parse

from flask import redirect, url_for, request, flash, render_template
from . import auth
from .. import db
from .forms import LoginForm, RegistrationForm
from app.models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
      return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
        flash('Invalid username or password')
        return redirect(url_for('auth.login'))
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('project.index')
    return redirect(next_page)
  return render_template('auth/login.html', title='Sign In', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('project.index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Congratulations, you are now a registered user!')
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html', title='Register', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('/'))