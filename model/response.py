from utils.files import write_cache
from classes.tsp_response import TspResponse
from classes.tsp_route import TspRoute

def generate_response(name, n, x, coordenadas, final_time, initial_time): 
    tspRoutes = get_routes(n, x, coordenadas)

    
    exec_time = final_time - initial_time
    response =  TspResponse(tspRoutes, exec_time).__dict__

    write_cache(f'./public/cache/{name}.json', response)


def get_routes(n, x, coordenadas): 
    routes = []
    expand = 3

    for i in range(n-1):
        for j in range(1, n):
            if round(x[i,j].primal) == 1:
                target = j

                if j == (n - 1):
                    target = 0

                route = TspRoute(i, target, coordenadas[i][0] * expand, coordenadas[i][1] * expand).__dict__
                routes.append(route)

    return routes