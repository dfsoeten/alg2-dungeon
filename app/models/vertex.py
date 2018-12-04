
class Vertex:

    id = -1

    passages = {}

    def __init__(self, id):
        self.id = id
        self.passages = {}

    def add_neighbor(self, vertex, weight):
        if vertex not in self.passages:
            self.passages[vertex] = weight

    def get_id(self):
        return self.id


