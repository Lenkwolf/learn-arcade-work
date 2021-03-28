import arcade

arcade.open_window(600,600, "Loss")

arcade.set_background_color((arcade.color.SPANISH_SKY_BLUE))

arcade.start_render()
arcade.draw_rectangle_filled(300, 150, 600, 300, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(215, 400, 20, 70, arcade.csscolor.BURLYWOOD)
arcade.draw_rectangle_filled(375, 400, 20, 70, arcade.csscolor.BURLYWOOD)
arcade.draw_rectangle_filled(400, 400, 20, 70, arcade.csscolor.BURLYWOOD)
arcade.draw_rectangle_filled(200, 210, 20, 70, arcade.csscolor.BURLYWOOD)
arcade.draw_rectangle_filled(225, 180, 20, 70, arcade.csscolor.BURLYWOOD)
arcade.draw_rectangle_filled(400, 170, 70, 20, arcade.csscolor.BURLYWOOD)
arcade.draw_rectangle_filled(350, 210, 20, 70, arcade.csscolor.BURLYWOOD)
arcade.finish_render()

arcade.run()