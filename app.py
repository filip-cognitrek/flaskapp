import datetime
from flask import Flask
app = Flask(__name__)


def stamp():
    return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


@app.route('/')
def hello_world():
    return f'Hello! Currently it is {stamp()}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
