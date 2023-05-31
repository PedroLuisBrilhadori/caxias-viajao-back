from flask import Flask

app = Flask(__name__)

@app.route('/routes')
def routes():
    return "Hello world!"


if __name__ == "__main__":
    app.run()