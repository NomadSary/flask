from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
USERS = {
    1: 'ALEX',
    2: 'NATALI',
    3: 'PITER',
}


@user.route('/')
def user_list():
    return render_template('user/list.html', users=USERS)


@user.route("/<int:pk>/")
# в роуте указан урл адрес для обращения
def user_details(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f"User #{pk} doesn't exist!")
    return render_template('user/datails.html', user_id=pk, user_name=user_name)
