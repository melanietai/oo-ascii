"""# print canvas with specified height and width
# add a shape to a canvas (rectangle)
# clear all shapes
# create a rectangle
start_x, start_y
                    end_x, end_y
fill_char = char used to draw the rectangle
# change the rectangle's fill character
# translate x axis to move left, right; translate y axis to move up, down
num is how much to move rectangle. -ve nums will shift left or down
"""

class Canvas:

    def __init__(self):
        self.shapes = []

    def render(self, height, width):
        
        for y in range(height):
            str = ''
            for x in range(width):
                fill_char = ' '
                for shape in self.shapes:
                    if shape.start_x <= x <= shape.end_x and shape.start_y <= y <= shape.end_y:
                        fill_char = shape.fill_char
                str += fill_char
            print(str)


    def add_shape(self, shape):
        self.shapes.append(shape)

    def clear_shapes(self):
        self.shapes = []

class Rectangle:

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char
    
    def change_fill_char(self, fill_char):
        self.fill_char = fill_char

    def translate(self, axis, num):
        if axis == "x":
            self.start_x += num
            self.end_x += num
        if axis == "y":
            self.start_y += num
            self.end_y += num
