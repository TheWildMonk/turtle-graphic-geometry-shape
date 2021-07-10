from turtle import Turtle, Screen


class Shape:
    def __init__(self, sides):
        self.sides = sides

    def calculate_shape(self):
        angle = 360/self.sides
        return angle


def move(geometry_shape):
    for each_side in range(geometry_shape):
        tim.right(Shape(geometry_shape).calculate_shape())
        tim.forward(100)


colors = ["LightSeaGreen", "DarkSlateBlue", "lawngreen", "HotPink4", "SpringGreen3", "tomato2", "OliveDrab4"]
tim = Turtle()
tim.shape("turtle")
for each_shape in range(3, 10):
    tim.color(colors[each_shape-3])
    move(each_shape)


screen = Screen()
screen.exitonclick()
