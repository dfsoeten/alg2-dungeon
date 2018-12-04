from .models.dungeon import Dungeon
from .views.renderer import Renderer


class Game:

    dungeon = None

    def __init__(self, config):
        self.dungeon = Dungeon(config['dungeon']['width'], config['dungeon']['height'])

    def start(self):
        (Renderer()).draw(self.dungeon)





