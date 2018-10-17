import json
from app.game import Game

# Get the configured dungeon width & height
with open('config.json') as file:
    game = (Game(json.load(file))).start()
