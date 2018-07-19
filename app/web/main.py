from flask import render_template
from flask_login import login_required, current_user
from . import web


@web.route('/')
def index():
    return 'index page'


@web.route('/personal')
@login_required
def personal_center():
    return render_template('personal.html', user=current_user.summary)


