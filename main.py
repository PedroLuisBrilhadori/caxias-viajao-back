from flask import Flask
from flask_cors import CORS
from tsp import*

app = Flask(__name__)
CORS(app)


@app.route('/routes')
def routes():
    dados = get_tsp_routes('./public/inst_10.txt')
    
    return dados


if __name__ == "__main__":
    app.run()

