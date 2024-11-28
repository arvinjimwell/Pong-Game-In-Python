import time
from turtle import Screen
from ball import Ball
from player import Player
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong: The Arcade Game")
screen.tracer(0)


r_player = Player(350)
l_player = Player(-350)
ball = Ball()

screen.listen()
screen.onkeypress(r_player.paddle.move_up, "Up")
screen.onkeypress(r_player.paddle.move_down, "Down")
screen.onkeypress(l_player.paddle.move_up, "w")
screen.onkeypress(l_player.paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    ball.bounce([l_player.paddle, r_player.paddle])
    if ball.xcor() < -450 or ball.xcor() > 450:
        if ball.xcor() < -450:
            r_player.increase_score()
        else:
            l_player.increase_score()

        ball.reset()
        screen.update()
        time.sleep(0.5)

screen.exitonclick()
