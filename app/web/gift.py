from flask import flash, current_app
from flask_login import login_required, current_user
from app.models.base import db
from app.models.gift import Gift
from . import web


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list():
        try:
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_PER_UPLOAD']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    else:
        flash('The book is already in wishlist.')


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    pass
