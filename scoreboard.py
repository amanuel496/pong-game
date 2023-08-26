from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Tilt Prism', 40, 'normal')


class Scoreboard(Turtle):

    def __init__(self, x_point, y_point, player):
        super().__init__()
        self.point = 0
        self.x_point = x_point
        self.y_point = y_point
        self.player = player
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.pencolor("white")
        self.penup()
        self.fillcolor("black")
        self.set_score()

    def set_score(self):
        self.goto(self.x_point, self.y_point)
        self.write(str(self.point), True, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increment_score(self):
        self.point += 1
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"{self.player}, you won!", align=ALIGNMENT, font=FONT)
