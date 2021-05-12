import arcade
import random

SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.5
COIN_COUNT = 50
MOVEMENT_SPEED = 10
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Coin(arcade.Sprite):

    def update(self):

        self.change_x = 0
        self.change_y = 0

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.bottom < 0:
            self.change_y = -1

        if self.top > SCREEN_HEIGHT:
            self.change_y = -1

class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(True)

    def setup(self):
        
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("Gorilla.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        arcade.set_background_color(arcade.color.GRAY)

        for i in range(COIN_COUNT):

            coin = Coin("coinGold.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)
    def on_draw(self):
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED 
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED 
        elif symbol == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif symbol == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player_sprite.change_y = 0

    def update(self, delta_time):

        self.coin_list.update()
        self.player_sprite.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()