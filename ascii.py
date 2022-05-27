"""
Object Oriented Programming Take-Home Practice
You'll be in charge of implementing the API for drawing rectangles (and squares). The API must be able to:

Render canvas with a specified height and width
Print the canvas and any shapes to standard output
Add a shape to a canvas
shape the shape to add. For now, assume you only have to deal with rectangles
Clear all shapes from a canvas
Create a rectangle
start_x is the X coordinate of the upper-left-hand corner of the rectangle
start_y is the Y coordinate of the upper-left-hand corner of the rectangle
end_x is the X coordinate of the lower-right-hand corner of the rectangle
end_y is the Y coordinate of the lower-right-hand corner of the rectangle
fill_char is the character that should be used to draw the rectangle
Change a rectangle's fill character
char the character to use in order to draw a pre-existing rectangle
Translate (move left, right, up, or down)
axis which axis ('x' or 'y') should we translate the rectangle on? Translating on the X-axis will cause the rectangle to move left and right. Translating on the Y-axis will cause the rectangle to move up and down.
num is how much to move the rectangle. Negative numbers will cause the rectangle to shift left or down. Positive numbers will cause the rectangle to shift right or up.
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

class Shape:

    def __init__(self, fill_char):
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

class Rectangle(Shape):

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        super().__init__(fill_char)
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

class Square(Shape):
    def __init__(self, start_x, start_y, length, fill_char):
        super().__init__(fill_char)
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = start_x + length - 1
        self.end_y = start_y + length - 1

