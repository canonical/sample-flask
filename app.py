import flask
from flask import Flask

app = Flask(__name__)
app.config.from_prefixed_env()


@app.route('/')
def index():
    return flask.render_template('index.html', greeting='Hello')


if __name__ == '__main__':
    app.run()
