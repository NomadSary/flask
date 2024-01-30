from flask import Flask, request

app = Flask(__name__)


@app.route('/<int:num>')
def index(num: int):
    name = request.args.get('name', None)
    return f'Hello {num} , {name}'
