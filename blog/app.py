from flask import Flask, render_template

from blog.index.index import index
from blog.user.users import user


# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')


#
# app.register_blueprint(user, url_prefix='/users')

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(index)
