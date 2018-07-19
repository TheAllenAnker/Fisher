from flask import redirect, render_template, flash
from flask import url_for, request
from flask_login import login_required, logout_user
from app.models.user import User
from . import web
from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from flask_login import login_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('Account doesn\'t exist or email and password don\'t match.' )
    return render_template('auth/login.html', form=form)


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


