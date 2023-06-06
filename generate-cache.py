from model.tsp import get_tsp_routes
from utils.files import read_file

cache = False 
name = 'inst_15'
data = read_file(f'./public/{name}.txt')

routes = get_tsp_routes(data, name, cache)
print(routes)