from flask import Flask, render_template
from blog.views.users import user

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(user, url_prefix='/users')