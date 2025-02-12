import arcade
import random
import PIL

# Set how many rows and columns we will have
ROW_COUNT = 24
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 0

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Tetris"

colors = [
          (199, 214, 156),
          (130, 143, 91),
          (126, 135, 99),
          (155, 166, 114),
          (115, 125, 80),
          (60, 64, 45),
          (118, 128, 79),
          (47, 51, 31),
          ]

# Define the shapes of the single parts
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]


def create_textures():
    """ Create a list of images for sprites based on the global colors. """
    new_textures = []
    for color in colors:
        # noinspection PyUnresolvedReferences
        image = PIL.Image.new('RGB', (WIDTH, HEIGHT), color)
        new_textures.append(arcade.Texture(str(color), image=image))
    return new_textures


texture_list = create_textures()


def rotate_counterclockwise(shape):
    """ Rotates a matrix clockwise """
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]


def check_collision(board, shape, offset):
    """
    See if the matrix stored in the shape will intersect anything
    on the board based on the offset. Offset is an (x, y) coordinate.
    """
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            if cell and board[cy + off_y][cx + off_x]:
                return True
    return False


def remove_row(board, row):
    """ Remove a row from the board, add a blank row on top. """
    del board[row]
    return [[0 for _ in range(COLUMN_COUNT)]] + board


def join_matrixes(matrix_1, matrix_2, matrix_2_offset):
    """ Copy matrix 2 onto matrix 1 based on the passed in x, y offset coordinate """
    offset_x, offset_y = matrix_2_offset
    for cy, row in enumerate(matrix_2):
        for cx, val in enumerate(row):
            matrix_1[cy + offset_y - 1][cx + offset_x] += val
    return matrix_1


def new_board():
    """ Create a grid of 0's. Add 1's to the bottom for easier collision detection. """
    # Create the main board of 0's
    board = [[0 for _x in range(COLUMN_COUNT)] for _y in range(ROW_COUNT)]
    # Add a bottom border of 1's
    board += [[1 for _x in range(COLUMN_COUNT)]]
    return board


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Set up the application. """

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.board = None
        self.frame_count = 0
        self.game_over = False
        self.paused = False
        self.board_sprite_list = None

        self.tetromino = None
        self.tetromino_x = 0
        self.tetromino_y = 0

    def new_tetromino(self):
        """
        Randomly grab a new tetromino and set the tetromino location to the top.
        If we immediately collide, then game-over.
        """
        self.tetromino = random.choice(tetris_shapes)
        self.tetromino_x = int(COLUMN_COUNT / 2 - len(self.tetromino[0]) / 2)
        self.tetromino_y = 0

        if check_collision(self.board, self.tetromino, (self.tetromino_x, self.tetromino_y)):
            self.game_over = True

    def setup(self):
        self.board = new_board()

        self.board_sprite_list = arcade.SpriteList()
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                sprite = arcade.Sprite()
                for texture in texture_list:
                    sprite.append_texture(texture)
                sprite.set_texture(0)
                sprite.center_x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                sprite.center_y = SCREEN_HEIGHT - (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                self.board_sprite_list.append(sprite)

        self.new_tetromino()
        self.update_board()

    def drop(self):
        """
        Drop the tetromino down one place.
        Check for collision.
        If collided, then
          join matrixes
          Check for rows we can remove
          Update sprite list with tetrominos
          Create a new tetromino
        """
        if not self.game_over and not self.paused:
            self.tetromino_y += 1
            if check_collision(self.board, self.tetromino, (self.tetromino_x, self.tetromino_y)):
                self.board = join_matrixes(self.board, self.tetromino, (self.tetromino_x, self.tetromino_y))
                while True:
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = remove_row(self.board, i)
                            break
                    else:
                        break
                self.update_board()
                self.new_tetromino()

    def rotate_tetromino(self):
        """ Rotate the tetromino, check collision. """
        if not self.game_over and not self.paused:
            new_tetromino = rotate_counterclockwise(self.tetromino)
            if self.tetromino_x + len(new_tetromino[0]) >= COLUMN_COUNT:
                self.tetromino_x = COLUMN_COUNT - len(new_tetromino[0])
            if not check_collision(self.board, new_tetromino, (self.tetromino_x, self.tetromino_y)):
                self.tetromino = new_tetromino

    def on_update(self, dt):
        """ Update, drop tetromino if warrented """
        self.frame_count += 1
        if self.frame_count % 20 == 0:
            self.drop()

    def move(self, delta_x):
        """ Move the tetromino back and forth based on delta x. """
        if not self.game_over and not self.paused:
            new_x = self.tetromino_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > COLUMN_COUNT - len(self.tetromino[0]):
                new_x = COLUMN_COUNT - len(self.tetromino[0])
            if not check_collision(self.board, self.tetromino, (new_x, self.tetromino_y)):
                self.tetromino_x = new_x

    def on_key_press(self, key, modifiers):
        """
        Handle user key presses
        User goes left, move -1
        User goes right, move 1
        Rotate tetromino,
        or drop down
        """
        if key == arcade.key.LEFT:
            self.move(-1)
        elif key == arcade.key.RIGHT:
            self.move(1)
        elif key == arcade.key.UP:
            self.rotate_tetromino()
        elif key == arcade.key.DOWN:
            self.drop()

    # noinspection PyMethodMayBeStatic
    def draw_grid(self, grid, offset_x, offset_y):
        """
        Draw the grid. Used to draw the falling tetrominos. The board is drawn
        by the sprite list.
        """
        # Draw the grid
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                # Figure out what color to draw the box
                if grid[row][column]:
                    color = colors[grid[row][column]]
                    # Do the math to figure out where the box is
                    x = (MARGIN + WIDTH) * (column + offset_x) + MARGIN + WIDTH // 2
                    y = SCREEN_HEIGHT - (MARGIN + HEIGHT) * (row + offset_y) + MARGIN + HEIGHT // 2

                    # Draw the box
                    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def update_board(self):
        """
        Update the sprite list to reflect the contents of the 2d grid
        """
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                v = self.board[row][column]
                i = row * COLUMN_COUNT + column
                self.board_sprite_list[i].set_texture(v)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        arcade.start_render()
        self.board_sprite_list.draw()
        self.draw_grid(self.tetromino, self.tetromino_x, self.tetromino_y)
        output = f"Tertis"
        arcade.draw_text(output, 120, 600, arcade.color.BLACK, 20)

def main():
    """ Create the game window, setup, run """
    my_game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    my_game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
