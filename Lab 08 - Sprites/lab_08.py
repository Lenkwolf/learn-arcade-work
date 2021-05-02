import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game(arcade.window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)