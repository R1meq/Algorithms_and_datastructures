class WeightedVertex:
    def __init__(self,index):
        self.neighbors = []
        self.weight_map = {}
        self.parent = None
        self.distance = 0
        self.index = index
