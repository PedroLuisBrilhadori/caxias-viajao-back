from sys import argv
from utils.files import read_file
from utils.graph import generate_graph


def main(): 

    if len(argv) == 1:
        return print('Command wrong. Please, try again. \n\nExample: \npython generate-cache.py ./filepath')
    
    name = "inst_25"
    
    name = argv.pop()
    

    data = read_file(f'./public/cache/{name}.json')
    generate_graph(data, name)

    print('graph saved!')

main()