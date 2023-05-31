class TspRoute: 
    id: str
    label: str
    targetId: str
    x: float
    y: float

    def __init__(self, id, targetId, x, y):
        self.id = str(id)
        self.label = str(id)
        self.targetId = str(targetId)
        self.x = x
        self.y = y
