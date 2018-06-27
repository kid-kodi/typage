# app/project/views.py

from flask import render_template
from flask_login import login_required

from . import project

@project.route('/project')
@login_required
def index():
  return render_template('project/index.html', title="Projects")

@project.route('/project/add')
@login_required
def add():
  return render_template('project/form.html', title="Projects")

@project.route('/project/edit/<int:id>')
@login_required
def edit(id):
  return render_template('project/form.html', title="Projects")

@project.route('/project/<int:id>')
@login_required
def detail(id):
  return render_template('project/detail.html', title="Projects")

@project.route('/project/download/<int:id>')
@login_required
def download(id):
  return render_template('project/download.html', title="Projects")

@project.route('/project/workspace/<int:id>')
@login_required
def workspace(id):
  return render_template('project/workspace.html', title="Projects")