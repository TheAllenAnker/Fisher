# Author: Allen Anker
# Created by Allen Anker on 14/07/2018
from app.libs.http_request import HTTP
from flask import current_app


class YuShuBook:
    """
    Acquire and store books data from API
    """
    # API addresses
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)
        return result

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'],
                                      self.__calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)
        return result

    @staticmethod
    def __calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']
