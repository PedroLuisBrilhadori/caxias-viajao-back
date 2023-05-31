class TspRoute: 
    id: str
    label: str
    targetId: str
    x: float
    y: float

    def __init__(self, id, targetId, x, y):
        self.id = id
        self.label = id
        self.targetId = targetId
        self.x = x
        self.y = y
