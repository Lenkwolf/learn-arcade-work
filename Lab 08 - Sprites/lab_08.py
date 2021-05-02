import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'shprite example')

        self.player_list = arcade.sprite_list()
        self.coin_list = arcade.sprite_list()

        self.score = 0

        self.player_sprite = arcade.Sprite("gorilla.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

def main():
    Window = Game()
    arcade.run

if __name__ == '__main__':
    main()