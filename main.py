# Pong Game
# Author: Amanuel Chukala
import time
from turtle import Screen

from ball import Ball
from line import Line
from paddle import Paddle


def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    print(screen.getshapes())
    ball = Ball()
    screen.tracer(0)

    court_line = Line()
    paddle_1 = Paddle(x_point=370, y_point=0)
    paddle_2 = Paddle(x_point=-370, y_point=0)
    screen.listen()
    screen.onkey(paddle_1.move_up, "Up")
    screen.onkey(paddle_1.move_down, "Down")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.03)
        ball.move()

        # Detection with wall
        if ball.get_x_point() > 400:
            game_is_on = False

        if ball.get_y_point() > 280 or ball.get_y_point() < -280:
            ball.move_test()

        # Detection with paddle
        if ball.distance(paddle_1) == 0:
            ball.setheading(180)

    screen.exitonclick()


if __name__ == '__main__':
    main()
