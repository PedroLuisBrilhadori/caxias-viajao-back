class TspResponse: 
    routes: list
    exec_time: float

    def __init__(self, routes, exec_time): 
        self.routes = routes
        self.exec_time = exec_time
