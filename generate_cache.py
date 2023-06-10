from sys import argv
from os.path import basename, exists
from model.tsp import get_tsp_routes
from utils.files import read_file


def main(): 
    if len(argv) == 1:
        return print('Command wrong. Please, try again. \n\nExample: \npython generate-cache.py ./filepath')
    
    custom_name = ''
    if len(argv) == 3: 
        custom_name = argv.pop()

    file_path = argv.pop()

    if exists(file_path): 
        return generate_cache(file_path, custom_name)
    
    return print(f'the file: {file_path} not exists')
    


def generate_cache(file_path, custom_name): 
    cache = False 
    data = ''
    name = basename(file_path).split('.')[0]
    
    if len(custom_name) > 0: 
        name = custom_name

    try: 
        data = read_file(file_path)
    except: 
        return print(f'could not read the file: {file_path} ')

    routes = get_tsp_routes(data, name, cache)
    print(routes)


main()