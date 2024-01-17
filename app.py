import flask
from flask import Flask

app = Flask(__name__)
app.config.from_prefixed_env()

TRANSLATIONS = {
    "ara": "مرحبا",
    "eng": "Hello",
    "fra": "Bonjour",
    "hin": "नमस्ते",
    "por": "Olá",
    "spa": "Hola",
    "swa": "Habari",
    "zho": "你好",
}


@app.route('/')
def index():
    language = app.config.get("LANGUAGE", "eng")
    return flask.render_template('index.html', greeting=TRANSLATIONS[language])


if __name__ == '__main__':
    app.run()
