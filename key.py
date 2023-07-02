import arcade
import os

class Key(arcade.Sprite):

    def __init__(self, char, location):
        super().__init__()
        self.center_x = location.x
        self.center_y = location.y
        self.char = char.upper()

        if char == "⌫":
            backspace_file_path = os.path.join("images", "keys", "backspace.png")
            backspace_texture = arcade.load_texture(backspace_file_path)
            self.textures.append(backspace_texture)
            self.set_texture(0)
            return
        elif char == "⏎":
            enter_file_path = os.path.join("images", "keys", "enter.png")
            enter_texture = arcade.load_texture(enter_file_path)
            self.textures.append(enter_texture)
            self.set_texture(0)
            return

        # everything else is A-Z
        # each character needs 4 textures - light_gray, gray, yellow, and green
        light_gray_file_path = os.path.join("images", "keys", "light_gray", f"{self.char}.png")
        gray_file_path = os.path.join("images", "keys", "gray", f"{self.char}.png")
        yellow_file_path = os.path.join("images", "keys", "yellow", f"{self.char}.png")
        green_file_path = os.path.join("images", "keys", "green", f"{self.char}.png")
        self.textures.append(arcade.load_texture(light_gray_file_path))
        self.textures.append(arcade.load_texture(gray_file_path))
        self.textures.append(arcade.load_texture(yellow_file_path))
        self.textures.append(arcade.load_texture(green_file_path))
        self.set_texture(0)

    def set_color(self, color):
        if color == '🟩':
            texture_index = 3
        elif color == '🟨':
            texture_index = 2
        else:
            texture_index = 1

        if texture_index > self.cur_texture_index:
            self.set_texture(texture_index)
