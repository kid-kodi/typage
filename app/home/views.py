# app/home/views.py

from flask import render_template
from flask_login import login_required, current_user

from . import home

@home.route('/')
@login_required
def index():
  return render_template('home/index.html', title="Welcome")