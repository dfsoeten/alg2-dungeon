from .vertex import Vertex


class Room(Vertex):

    start = False

    end = False

    visited = False

    def __init__(self, id):
        Vertex.__init__(self, id)

    def set_start(self, start):
        self.start = start

    def is_start(self):
        return self.start

    def set_end(self, end):
        self.end = end

    def is_end(self):
        return self.end

    def get_character(self):
        if self.start:
            return 'S'
        if self.end:
            return 'E'
        if not self.visited:
            return 'X'
        else:
            return '*'



