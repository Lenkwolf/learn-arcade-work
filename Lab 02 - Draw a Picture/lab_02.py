import arcade

WIDTH = 800
HEIGHT = 800


def on_draw(dt):
    arcade.start_render()


    arcade.draw_circle_filled(on_draw.x,on_draw.y,50,arcade.color.RED)
    on_draw.x += 1
    on_draw.y += 3


on_draw.x = 100
on_draw.y = 100

arcade.open_window(WIDTH,HEIGHT,'bounce')
arcade.set_background_color(arcade.color.GRAY)
arcade.schedule(on_draw, 1/60)




arcade.run()