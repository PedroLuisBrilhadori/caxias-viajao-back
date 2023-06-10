import json
from matplotlib.pyplot import text, savefig, annotate, scatter, plot


def generate_graph(json_data, name):
    data = json.loads(json_data)

    pontos = {route['id']: {'x': route['x'], 'y': route['y']} for route in data['routes']}

    for route in data['routes']:
        x_start, y_start = pontos[route['id']]['x'], pontos[route['id']]['y']
        x_end, y_end = pontos[route['targetId']]['x'], pontos[route['targetId']]['y']
        plot([x_start, x_end], [y_start, y_end], 'k-', zorder=0)

    for route in data['routes']: 
        if route['id'] == '0': 
            scatter(route['x'], route['y'], color='green', marker='o')
        else:
            scatter(route['x'], route['y'], color='red', marker='o')


    savefig(f'./public/images/{name}')
