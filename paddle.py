from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 40
UPPER_LIMIT = 243
LOWER_LIMIT = -241


class Paddle(Turtle):

    def __init__(self, x_point, y_point, name):
        super().__init__()
        self.name = name
        self.x_point = x_point
        self.y_point = y_point
        self.stick = Turtle()
        self.create_stick()

    def create_stick(self):

        self.stick.shape("square")
        self.stick.color("white")
        self.stick.shapesize(stretch_wid=.5, stretch_len=2.5)
        self.stick.setheading(90)
        self.stick.penup()
        self.stick.goto((self.x_point, self.y_point))

    def move_up(self):

        if self.stick.ycor() < UPPER_LIMIT:
            self.stick.setheading(UP)
            self.stick.forward(MOVE_DISTANCE)

    def move_down(self):

        if self.stick.ycor() > LOWER_LIMIT:
            self.stick.setheading(DOWN)
            self.stick.forward(MOVE_DISTANCE)

    def get_position(self):
        return self.stick.position()
