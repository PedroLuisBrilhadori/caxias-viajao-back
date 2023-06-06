from pymprog import iprod, begin, minimize, solve, end, var, solver, vobj
from time import time
from model.response import generate_response
from model.variables import variables
from model.constraints import constraints, exclude_sub_routes
import json


def get_tsp_routes(data, name, cache = True): 
    if cache: 
        try:
            return get_tsp_cache(name)
        except: 
            print('no')

    return calc_tsp_routes(data, name)        


def get_tsp_cache(name): 
    with open(f'./public/cache/{name}.json') as file: 
        return json.load(file)


def calc_tsp_routes(data, name): 
    initial_time = time(); 

    begin(f'caixeiro - {initial_time}') # Início do modelo

    n, coordenadas, tempoDeServico, deadline, M = variables(data)
    print(n, coordenadas, tempoDeServico, deadline, M)

    prod = iprod(range(n), range(n))

    # variaveis de decisão

    x = var("x", prod, bool)
    
    # Quantifica o atraso em cada nó
    z = var("z", n) 
    
    # Variável que representa o instante de início do tempo de serviço, realizando o acumulo de tempo decorrido
    phi = var("phi", n) 

    # Modelo / Função Objetivo
    minimize(sum(z[j] for j in range(1, n-1))) 

    x = constraints(n, x)

    x, z, phi = exclude_sub_routes(n, x, z, phi, M, coordenadas, tempoDeServico, deadline)

    solver(int, gmi_cuts = 1)
    solver(int, tm_lim = 3600 * 1000)

    solve()
    great_value = vobj()
    end()
    
    final_time = time()


    return generate_response(name, n, x, coordenadas, final_time, initial_time, great_value)




