# Author: Allen Anker
# Created by Allen Anker on 14/07/2018


from flask import jsonify, request
from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.book import SearchForm


@web.route('/book/search')
def search():
    """
    :q: search key word
    :page: how many results
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify({'msg':'args validation failed'})
