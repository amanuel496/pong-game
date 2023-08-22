from turtle import Turtle

RATIO = .5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.create_ball()

    def create_ball(self):
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.shapesize(stretch_wid=RATIO, stretch_len=RATIO)
        self.ball.penup()
        self.ball.speed(0)

    def move(self):
        if self.ball.xcor() >= 360:
            # self.ball.setheading(randint(160, 200))
            self.ball.setheading(270)
        self.ball.forward(20)

    def move_test(self):
        self.ball.setheading(160)
        self.ball.forward(20)

        # NOTE: For collision between ball and wall/paddle
        # Randomly select heading of the ball based on the direction it's heading

    def get_x_point(self):
        return self.ball.xcor()

    def get_y_point(self):
        return self.ball.ycor()
