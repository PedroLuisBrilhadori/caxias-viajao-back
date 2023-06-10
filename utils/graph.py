import json
from matplotlib.pyplot import text, savefig, scatter, plot


def generate_graph(json_data, name):
    data = json.loads(json_data)

    pontos = {route['id']: {'x': route['x'], 'y': route['y']} for route in data['routes']}

    for route in data['routes']:
        x_start, y_start = pontos[route['id']]['x'], pontos[route['id']]['y']
        x_end, y_end = pontos[route['targetId']]['x'], pontos[route['targetId']]['y']
        plot([x_start, x_end], [y_start, y_end], 'k-', zorder=0)

    first_id = ''
    
    for route in data['routes']:
        color = 'red' 
        
        if route['id'] == '0': 
            color = 'green'
            first_id = route['targetId']
        
        if route['id'] == first_id: 
            color = 'blue'

        if route['targetId'] == '0': 
            color = 'black'

        scatter(route['x'], route['y'], color=color, marker='o', s=100)

    for route in data['routes']:
        x_end, y_end = pontos[route['targetId']]['x'], pontos[route['targetId']]['y']
        text(x_end, y_end - 0.2, route['label'], ha='center', va='center', color="white", fontsize=8, fontweight='bold')

    savefig(f'./public/images/{name}')
