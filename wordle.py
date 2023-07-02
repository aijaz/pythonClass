# Basic arcade program using objects
# Displays a white window with a blue circle in the middle

# Imports
import arcade

import game
from point import Point
from cell import Cell
from key import Key

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Wordle"
RADIUS = 150
MAX_GUESSES = 6


# Classes
class WordleWindow(arcade.Window):
    """Main welcome window
    """
    def __init__(self, color):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background window
        arcade.set_background_color(color)

        # create a list of lists of cells
        self.cell_sprite_lists = []  # self.cells is a list of arcade.SpriteLists
        for n in range(MAX_GUESSES):
            self.cell_sprite_lists.append(arcade.SpriteList())


        # create a list of keys
        self.keys = arcade.SpriteList()

        # create a reverse lookup from character to sprite
        self.keys_by_char = {}

        # create the sprites that I need
        # first, create the keys
        self.create_keys()
        self.create_cells()

        # game variables
        self.current_guess = ""
        self.current_guess_number = 0
        self.game_over = False
        self.secret_word = game.get_random_word()
        self.should_show_secret_word = False

    def create_keys(self):
        key_width = 36
        key_height = 60
        start_x = 105
        delta_x = 8
        delta_y = 8

        # create the first row of keys
        location = Point(x=start_x, y=300)
        for char in "QWERTYUIOP":
            current_key = Key(char, location)
            self.keys_by_char[char] = current_key  # create the reverse lookup
            self.keys.append(current_key)
            location.x += key_width + delta_x

        # create the second row of keys
        location.x = start_x
        location.x += key_width/2
        location.y -= (key_height + delta_y)
        for char in "ASDFGHJKL":
            current_key = Key(char, location)
            self.keys_by_char[char] = current_key  # create the reverse lookup
            self.keys.append(current_key)
            location.x += key_width + delta_x

        # create the third row of keys
        location.x = start_x + key_width + delta_x + key_width/2
        location.y -= (key_height + delta_y)
        for char in "ZXCVBNM":
            current_key = Key(char, location)
            self.keys_by_char[char] = current_key  # create the reverse lookup
            self.keys.append(current_key)
            location.x += key_width + delta_x

        # create backspace
        location.x += 9
        current_key = Key("⌫", location)
        self.keys.append(current_key)

        # create enter
        location.x = start_x + key_width - 27
        current_key = Key("⏎", location)
        self.keys.append(current_key)

    def create_cells(self):
        image_width = 56
        image_height = 56
        delta_x = image_width + 2
        delta_y = image_height + 2
        top_margin = 50
        window_center_x = SCREEN_WIDTH // 2

        # once I have top_left, I don't want to change it.
        top_left = Point(x=window_center_x - (delta_x * 2), y=SCREEN_HEIGHT - top_margin)

        # the location of the current cell
        current_location = top_left.clone()

        for row in range(MAX_GUESSES):
            current_location.x = top_left.x

            for c in range(5):
                cell = Cell(current_location)
                self.cell_sprite_lists[row].append(cell)
                current_location.x += delta_x  # the next cell will be delta_x to the right

            current_location.y -= delta_y

    def on_draw(self):
        """Called whenever you need to draw your window
        """
        # clear the screen

        # draw each sprite list
        for sprite_list in self.cell_sprite_lists:
            sprite_list.draw()

        # draw the keys
        self.keys.draw()

        # show the secret word if necessary
        if self.should_show_secret_word:
            arcade.draw_text(self.secret_word,
                         SCREEN_WIDTH/2 - 35,
                         375,
                         arcade.color.WHITE,
                         18, bold=True)


    def on_key_release(self, key_code: int, modifiers: int):
        if arcade.key.A <= key_code <= arcade.key.Z:
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.handle_letter_press(chars[key_code - arcade.key.A])
        elif key_code == arcade.key.BACKSPACE:
            self.handle_backspace()
        elif key_code == arcade.key.ENTER or key_code == arcade.key.RETURN:
            self.handle_enter()

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        pressed_keys = arcade.get_sprites_at_point((x, y), sprite_list=self.keys)
        if pressed_keys:
            key = pressed_keys[0]
            char = key.char
            if char == '⌫':
                self.handle_backspace()
            elif char == '⏎':
                self.handle_enter()
            else:
                self.handle_letter_press(char)

    def handle_letter_press(self, char):
        if self.game_over:
            return

        # if our guess is already 5 letters long, don't allow the user to add a 6th letter
        if len(self.current_guess) == 5:
            return
        self.current_guess += char
        guess_length = len(self.current_guess)
        cell_index = guess_length - 1

        sprite_list_index = self.current_guess_number
        self.cell_sprite_lists[sprite_list_index][cell_index].set_char(char)

    def handle_backspace(self):
        guess_length = len(self.current_guess)
        if guess_length > 0:
            self.current_guess = self.current_guess[:-1]  # drop off the loast character from current guess
            cell_index = guess_length - 1
            sprite_list_index = self.current_guess_number
            self.cell_sprite_lists[sprite_list_index][cell_index].clear()

    def handle_enter(self):
        if len(self.current_guess) != 5:
            return

        if self.current_guess not in game.guessable_words:
            return

        result = game.get_result(self.secret_word, self.current_guess)

        # update the cells
        for n, emoji in enumerate(result):
            self.cell_sprite_lists[self.current_guess_number][n].set_color(emoji)

        # did we guess the correct word?
        if self.current_guess == self.secret_word:
            self.game_over = True
            return

        # if the word is not the secret word
        self.current_guess_number += 1
        self.current_guess = ""

        if self.current_guess_number == MAX_GUESSES:
            self.game_over = True
            self.should_show_secret_word = True


# Main code entry point
if __name__ == "__main__":
    app = WordleWindow(arcade.color.BLACK)
    arcade.run()