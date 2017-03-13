from app import app, db, login_manager
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from flask_login import (
    login_user,
    logout_user,
    current_user,
    login_required,
)
from .forms import LoginForm, SignupForm
from .models import Equipo, Integrante


@app.route('/')
def index():
    render_template('index')
