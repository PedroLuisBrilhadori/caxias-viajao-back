class TspResponse: 
    routes: list
    exec_time: float
    great_value: any

    def __init__(self, routes, exec_time, great_value): 
        self.routes = routes
        self.exec_time = exec_time
        self.great_value = great_value
