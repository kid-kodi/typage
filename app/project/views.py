# app/project/views.py

from flask import render_template
from flask_login import login_required

from . import project

@project.route('/project')
def index():
  return render_template('project/index.html', title="Projects")

@project.route('/project/add')
def add():
  return render_template('project/form.html', title="Projects")

@project.route('/project/edit/<int:id>')
def edit(id):
  return render_template('project/form.html', title="Projects")

@project.route('/project/<int:id>')
def detail(id):
  return render_template('project/detail.html', title="Projects")

@project.route('/project/download/<int:id>')
def download(id):
  return render_template('project/download.html', title="Projects")

@project.route('/project/workspace/<int:id>')
def workspace(id):
  return render_template('project/workspace.html', title="Projects")