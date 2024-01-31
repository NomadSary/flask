from flask import Blueprint, render_template


index = Blueprint('index', __name__, url_prefix='/', static_folder='../static')


@index.route('/')
def index_1():
    return render_template('index/index.html')



