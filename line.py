from turtle import Turtle

POSITIONS = [(0, 284), (0, 252), (0, 220), (0, 188), (0, 156), (0, 124), (0, 92), (0, 60), (0, 28), (0, -4), (0, -36),
             (0, -68), (0, -100), (0, -132), (0, -164), (0, -196), (0, -228), (0, -260)]


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.lines = []
        self.create_table_lines()

    def create_table_lines(self):

        for position in POSITIONS:
            new_line = Turtle("square")
            new_line.color("white")
            new_line.speed("fastest")
            new_line.shapesize(stretch_wid=.2, stretch_len=.8)
            new_line.setheading(90)

            new_line.penup()
            new_line.goto(position)
            self.lines.append(new_line)
