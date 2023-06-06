class TspRoute: 
    id: str
    label: str
    targetId: str
    x: int
    y: int
    def __init__(self, id, targetId, x, y):
        self.id = str(id)
        self.label = str(id)
        self.targetId = str(targetId)
        self.x = x
        self.y = y

class TspResponse: 
    routes: list
    exec_time: float

    def __init__(self, routes, exec_time): 
        self.routes = routes
        self.exec_time = exec_time
