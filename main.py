from flask import Flask, request
from flask_cors import CORS
from tsp import get_tsp_routes

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# TODO: body validator
@app.route('/routes', methods=['POST'])
def routes():   
    cache = request.json['cache']
    data = request.json['data']
    name = request.json['name']

    dados = get_tsp_routes(data, name, cache)
    
    return dados


if __name__ == "__main__":
    app.run()

