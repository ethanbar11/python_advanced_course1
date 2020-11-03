from flask import Flask, request
import random

app = Flask(__name__)


@app.route('/new_user/<user_name>')
def add_user(user_name):
    return "The user {} has been added".format(user_name)


@app.route('/', methods=['GET'])
def get_random():
    return str(random.randint(0, 100))


@app.route('/hello', methods=['POST'])
def hello_world():
    return 'Hello world!'


@app.route('/blibla', methods=['GET', 'POST'])
def klik():
    return str(5 + 3 / 2)


@app.route('/woho', methods=['POST'])
def get_woho():
    x = request.get_json()
    for i in x.keys():
        print(i)
    return "Success!"


if __name__ == '__main__':
    app.run()
