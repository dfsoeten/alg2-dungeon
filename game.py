from .models.dungeon import Dungeon

class Game:

    dungeon = None

    def __init__(self, config):
        self.dungeon = Dungeon(config['dungeon']['width'], config['dungeon']['height'])

