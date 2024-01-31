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


@user.route("/<int:user_id>/")
def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template('user/datails.html', user_id=user_id, user_name=user_name)