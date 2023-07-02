import os
import arcade


class Cell(arcade.Sprite):

    def __init__(self, location):
        super().__init__()
        path_to_blank_image = os.path.join("images", "cells", "blank", "BLANK.png")
        blank_texture = arcade.load_texture(path_to_blank_image)  # create a texture

        # add the texture to the list of textures for this sprite
        self.append_texture(blank_texture)

        # which texture do we want to display right now?
        self.set_texture(0)

        # move this cell to the proper location
        self.center_x = location.x
        self.center_y = location.y

        self.char = ''

    def set_char(self, char):
        gray = os.path.join("images", "cells", "gray", f"{char.upper()}.png")
        yellow = os.path.join("images", "cells", "yellow", f"{char.upper()}.png")
        green = os.path.join("images", "cells", "green", f"{char.upper()}.png")
        current = os.path.join("images", "cells", "current", f"{char.upper()}.png")

        # TODO: FILL IN THIS FUNCTION
        self.textures = self.textures[:1]  # remove all but the first texture
        self.append_texture(arcade.load_texture(gray))
        self.append_texture(arcade.load_texture(yellow))
        self.append_texture(arcade.load_texture(green))
        self.append_texture(arcade.load_texture(current))
        self.set_texture(4)
        self.char = char

    def clear(self):
        self.set_texture(0)
        self.textures = self.textures[:1]

    def set_color(self, emoji):
        if emoji == '🟩':
            texture_index = 3
        elif emoji == '🟨':
            texture_index = 2
        else:
            texture_index = 1

        self.set_texture(texture_index)
