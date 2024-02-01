from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.user.users import USERS

articles = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')
ARTICLES = {
    1: {
        'test': 'gvzbfsdgbfadbg',
        'author': 1
    },
    2: {
        'test': 'lorem23',
        'author': 2
    },
    3: {
        'test': 'lorem23',
        'author': 3
    },
    4: {
        'test': 'lorem23',
        'author': 1
    }
}


@articles.route('/')
def articles_list():
    return render_template('articles/article_list.html', articles=ARTICLES)


@articles.route("/<int:pk>/")
# в роуте указан урл адрес для обращения
def articles_details(pk: int):
    try:
        artik = ARTICLES[pk]
    except KeyError:
        raise NotFound(f"artik #{pk} doesn't exist!")
    return render_template('articles/article_detalis.html', artik_id=pk, artik_name=artik ,authors=USERS)
