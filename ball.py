from turtle import Turtle

RATIO = .5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.create_ball()
        self.angles_paddle_1 = [115, 130, 145, 160, 200, 215, 230, 245]
        self.angles_paddle_2 = [15, 30, 45, 60, 300, 315, 330, 345]

    def create_ball(self):
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.shapesize(stretch_wid=RATIO, stretch_len=RATIO)
        self.ball.penup()
        self.ball.speed(0)
        self.ball.setheading(0)

    def move(self, detected_item=None, paddle_name=None):

        if detected_item == "wall":

            # If the ball is in Quadrant I
            if (self.ball.xcor() >= 0 and self.ball.ycor() >= 0) and paddle_name == "paddle_1":
                self.ball.setheading(200)

            elif (self.ball.xcor() >= 0 and self.ball.ycor() >= 0) and paddle_name == "paddle_2":
                self.ball.setheading(300)

            # If the ball is in Quadrant II
            if (self.ball.xcor() <= 0 <= self.ball.ycor()) and paddle_name == "paddle_1":
                self.ball.setheading(230)

            if (self.ball.xcor() <= 0 <= self.ball.ycor()) and paddle_name == "paddle_2":
                self.ball.setheading(345)

            # If the ball is in Quadrant III
            if self.ball.xcor() < 0 and self.ball.ycor() < 0 and paddle_name == "paddle_1":
                self.ball.setheading(300)

            if self.ball.xcor() < 0 and self.ball.ycor() < 0 and paddle_name == "paddle_2":
                self.ball.setheading(60)

            # If the ball is in Quadrant IV
            if (self.ball.xcor() > 0 > self.ball.ycor()) and paddle_name == "paddle_1":
                self.ball.setheading(145)

            if (self.ball.xcor() > 0 > self.ball.ycor()) and paddle_name == "paddle_2":
                self.ball.setheading(15)

        if detected_item == "paddle":

            if paddle_name == "paddle_1":
                self.ball.setheading(245)

            elif paddle_name == "paddle_2":
                self.ball.setheading(330)

        self.ball.forward(20)

    def refresh(self):
        # self.ball.setheading(choice([0,180]))
        self.ball.setheading(0)
        self.ball.goto(0, 0)

        # NOTE: For collision between ball and wall/paddle
        # Randomly select heading of the ball based on the direction it's heading

    def get_x_point(self):
        return self.ball.xcor()

    def get_y_point(self):
        return self.ball.ycor()

    def get_heading(self):
        return self.ball.heading()

    def get_distance(self, paddle_cor):
        return self.ball.distance(paddle_cor)
