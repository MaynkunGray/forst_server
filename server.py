from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def image_a():
    return f'''<img src="{url_for('static', filename='img/Кот на арбузе.jpeg')}">'''


@app.route("/apple")
def image_ya():
    return f'''<img src="{url_for('static', filename='img/Кот на яблоке.webp')}">'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
