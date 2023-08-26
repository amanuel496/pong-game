# Pong Game
# Author: Amanuel Chukala
import time
from turtle import Screen

from ball import Ball
from line import Line
from paddle import Paddle
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    ball = Ball()
    screen.tracer(0)

    court_line = Line()
    paddle_1 = Paddle(x_point=370, y_point=0, name="paddle_1")
    paddle_2 = Paddle(x_point=-370, y_point=0, name="paddle_2")
    score_1 = Scoreboard(x_point=50, y_point=230, player="Player_1")
    score_2 = Scoreboard(x_point=-50, y_point=230, player="Player_2")
    screen.listen()
    screen.onkey(paddle_1.move_up, "Up")
    screen.onkey(paddle_1.move_down, "Down")

    screen.onkey(paddle_2.move_up, "w")
    screen.onkey(paddle_2.move_down, "s")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.001)
        ball.move()

        # Detection with wall
        if ball.get_x_point() > 400:
            score_2.increment_score()
            score_2.set_score()
            ball.refresh()
            if score_2.point == 10:
                court_line.call_hiding_function()
                score_2.game_over()
                game_is_on = False

        if ball.get_x_point() < -400:
            score_1.increment_score()
            score_1.set_score()
            ball.refresh()
            if score_1.point == 10:
                court_line.call_hiding_function()
                score_1.game_over()
                game_is_on = False
        if ball.get_y_point() > 285 or ball.get_y_point() < -280:
            if ball.get_heading() in ball.angles_paddle_1:
                ball.move(detected_item="wall", paddle_name=paddle_1.name)
            elif ball.get_heading() in ball.angles_paddle_2:
                ball.move(detected_item="wall", paddle_name=paddle_2.name)

        # Detection with paddle
        if ball.get_distance(paddle_1.get_position()) < 12:
            ball.move(detected_item="paddle", paddle_name=paddle_1.name)

        if ball.get_distance(paddle_2.get_position()) < 12:
            ball.move(detected_item="paddle", paddle_name=paddle_2.name)

    screen.exitonclick()


if __name__ == '__main__':
    main()
