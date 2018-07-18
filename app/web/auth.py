from flask import redirect, render_template
from flask import url_for
from flask_login import login_required, logout_user
from . import web


@web.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
@login_required
def change_password():
    pass


@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.index'))


@web.route('/register/confirm/<token>')
def confirm(token):
    pass


@web.route('/register/ajax', methods=['GET', 'POST'])
def register_ajax():
    pass


