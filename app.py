import datetime
import os

import flask
import psycopg2
from flask import Flask, request

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

DATABASE_URI = os.environ["POSTGRESQL_DB_CONNECT_STRING"]


@app.route('/')
def index():
    with psycopg2.connect(DATABASE_URI) as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visitors (
                timestamp TIMESTAMP NOT NULL,
                user_agent TEXT NOT NULL
            );
        """)

        user_agent = request.headers.get('User-Agent')
        timestamp = datetime.datetime.now()
        cur.execute(
            "INSERT INTO visitors (timestamp, user_agent) VALUES (%s, %s)",
            (timestamp, user_agent)
        )

        cur.execute("SELECT COUNT(*) FROM visitors")
        total_visitors = cur.fetchone()[0]

        conn.commit()

    language = app.config.get("LANGUAGE", "eng")
    return flask.render_template(
        'index.html',
        greeting=TRANSLATIONS[language],
        visitors=total_visitors
    )


if __name__ == '__main__':
    app.run()
