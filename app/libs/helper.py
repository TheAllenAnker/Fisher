# Author: Allen Anker
# Created by Allen Anker on 14/07/2018


def is_isbn_or_key(word):
    """
    Determine the search key word is ISBN or others
    :param word: the search key word
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_q = word.replace('-', '')
    if '-' in word and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key