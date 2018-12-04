from .vertex import Vertex
from .room import Room
import random


class Dungeon:
    rooms = {}

    width = -1

    height = -1

    def __init__(self, width, height):
        """
        Creates a dungeon (graph) with rooms (vertices) equal to the width and height as defined in config.json.
        Initializes this dungeon with random passages (edges)
        """
        self.width = width
        self.height = height

        # Add rooms
        for i in range(self.width * self.height):
            self.add_room(Room(i))

        # Add passages
        for y in range(self.height):
            for x in range(self.width):
                i = x + (self.width * y)

                if not y & 1 and x != 0 and x != self.width - 1:
                    self.add_passage(i, i - 1)
                    self.add_passage(i, i + 1)
                self.add_passage(i, i - width)
                self.add_passage(i, i + width)

    def add_room(self, room):
        """
        Creates a room (vertices) and adds it to the dungeon. Returns True if it succeeded, False when not.
        :param room:
        :return:
        """
        if isinstance(room, Vertex) and not self.has_room(room.get_id()):
            self.rooms[room.get_id()] = room
            return True
        else:
            return False

    def has_room(self, room):
        """
        Checks if a room exists by index.

        :param room:
        :return:
        """
        return room in self.rooms

    def add_passage(self, from_room, to_room, weight=-1):
        """
        Adds a weighted passage (edge) between rooms (vertices). The weight of the passage defines the strength of
        the enemy in it.

        :param from_room:
        :param to_room:
        :param weight:
        :return:
        """
        if from_room in self.rooms and to_room in self.rooms:
            weight = random.randint(0, 9) if weight == -1 else weight

            for key, value in self.rooms.items():
                if key == from_room:
                    value.add_neighbor(to_room, weight)
                if key == to_room:
                    value.add_neighbor(from_room, weight)

    def add_random_passage(self, amount):
        """
        Adds a random amount of passages (edges) to the dungeon (graph). Uses recursion to avoid adding a passage to
        itself or a passage that already exists.

        :param amount:
        :return:
        """
        for i in range(amount):
            from_room = random.randint(0, (len(self.rooms) - 1))
            to_room = random.randint(0, (len(self.rooms) - 1))

            if not self.rooms[from_room].has_passage(to_room) and from_room != to_room:
                self.add_passage(from_room, to_room, random.randint(0, 3))
            else:
                self.add_random_passage(1)

    def bfs(self, start):
        """

        :param start:
        :return:
        """
        visited, queue = set(), [start]

        while queue:
            vertex = queue.pop(0)

            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(self.rooms[vertex].get_passages()) - visited)

        return visited

    def bfs_paths(self, from_room, to_room):
        """
        Gets all paths between two rooms (vertices).

        :param from_room:
        :param to_room:
        :return:
        """
        queue = [(from_room, [from_room])]

        while queue:
            (room, path) = queue.pop(0)
            for next_room in set(self.rooms[room].get_passages()) - set(path):
                if next_room == to_room:
                    yield path + [next_room]
                else:
                    queue.append((next_room, path + [next_room]))

    def shortest_path(self, start, goal):
        """
        Gets the shortest path from one room to another.

        :param start:
        :param goal:
        :return:
        """
        try:
            return next(self.bfs_paths(start, goal))
        except StopIteration:
            return None

    def get_room(self, index):
        """
        Get room by index

        :param index:
        :return:
        """
        return self.rooms[index]









