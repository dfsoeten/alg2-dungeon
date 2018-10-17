from game import Game

# Get the configured dungeon width & height
with open('config.json') as config:
    game = Game(config)
