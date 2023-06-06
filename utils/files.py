from json import dumps

def write_cache(file, routes): 
    with open(file, 'w') as file: 
        file.write(dumps(routes))
        file.close()

def read_file(file): 
      with open(file) as f:
        data = f.read()
        return data
