# Author: Allen Anker
# Created by Allen Anker on 14/07/2018
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish