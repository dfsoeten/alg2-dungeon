

class Renderer:

    def __init__(self):
        pass

    def draw(self, dungeon):
        for key, value in dungeon.rooms.items():
            print(value.get_character(), end=' ')
            if (key + 1) % dungeon.width == 0:
                print()

    def debug(self, dungeon):
        for key, value in dungeon.rooms.items():
            print(str(key) + str(value.get_passages()))

