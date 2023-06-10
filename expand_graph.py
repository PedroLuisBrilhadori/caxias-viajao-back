import json
from utils.files import read_file, write_cache

def divide_valores_por_3(routes):
    for route in routes:
        route['x'] //= 3
        route['y'] //= 3
    return routes

def main():
    file_name = 'inst_25' 
    file_path = f'./public/cache/{file_name}.json'

    file_data = read_file(file_path)

    tspResponse = json.loads(file_data)

    tspResponse['routes'] = divide_valores_por_3(tspResponse['routes'])

    write_cache(file_path, tspResponse)
    print('cache saved')
main()