import arcade

WIDTH = 800
HEIGHT = 800


def on_draw(dt):
    arcade.start_render()


    arcade.draw_circle_filled(on_draw.x,on_draw.y,50,arcade.color.RED)
    on_draw.x += on_draw.vx
    on_draw.y += on_draw.vy
    if on_draw.x < 0:
        on_draw.vx =abs(on_draw.vx)
    if on_draw.x < WIDTH:
        on_draw.vx =abs(on_draw.vx)
    if on_draw.y < 0:
        on_draw.vy =abs(on_draw.vy)
    if on_draw.x < 0:
        on_draw.vx =abs(on_draw.vx)
on_draw.x = 100
on_draw.y = 100

on_draw.vx = 2
on_draw.vy = 2
arcade.open_window(WIDTH,HEIGHT,'bounce')
arcade.set_background_color(arcade.color.GRAY)
arcade.schedule(on_draw, 1/60)




arcade.run()