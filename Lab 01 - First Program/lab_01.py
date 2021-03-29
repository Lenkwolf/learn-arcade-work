import arcade

arcade.open_window(600,600, "A")

arcade.set_background_color((arcade.color.PURPLE_TAUPE))

arcade.start_render()
arcade.draw_circle_filled(300,300,50,arcade.csscolor.DARK_ORANGE)
arcade.draw_rectangle_filled(300, 150, 600, 300, arcade.csscolor.DARK_SLATE_BLUE)
arcade.draw_triangle_filled(0,300,0,400,235,300,arcade.csscolor.PURPLE)
arcade.draw_triangle_filled(100,350,180,350,235,300,arcade.csscolor.PURPLE)
arcade.draw_triangle_filled(0,300,100,370,180,300,arcade.color.DARK_PASTEL_PURPLE)
arcade.draw_triangle_filled(100,300,175,325,225,300,arcade.color.DARK_PASTEL_PURPLE)
arcade.draw_triangle_filled(600,300,600,400,365,300,arcade.csscolor.PURPLE)
arcade.draw_triangle_filled(500,350,420,350,365,300,arcade.csscolor.PURPLE)
arcade.draw_triangle_filled(600,300,500,370,420,300,arcade.color.DARK_PASTEL_PURPLE)
arcade.draw_triangle_filled(500,300,425,325,375,300,arcade.color.DARK_PASTEL_PURPLE)
arcade.draw_lines(((250,300),
    	            (200,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((350,300),
    	            (400,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((200,300),
    	            (100,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((150,300),
    	            (-25,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((100,300),
    	            (-150,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((50,300),
    	            (-275,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((400,300),
    	            (475,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((450,300),
    	            (575,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((500,300),
    	            (675,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((550,300),
    	            (775,0),
),
                    arcade.csscolor.BLUE)
arcade.draw_lines(((300,300),
    	            (300,0),
),
                    arcade.csscolor.BLUE)




arcade.finish_render()

arcade.run()