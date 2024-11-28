from turtle import Turtle
from paddle import Paddle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movement = random.choice([1, -1])
        self.y_movement = 0
        self.reset()

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce(self, paddles:[Paddle]):
        if self.ycor() > 285 and self.y_movement > 1:
            self.change_y_direction()
        elif self.ycor() < -285 and self.y_movement < -1:
            self.change_y_direction()

        for paddle in paddles:
            if self.distance(paddle) < 70 and (self.xcor() > 320 or self.xcor() < -320):
                speed = random.randint(15, 20)
                if self.x_movement > 1 and paddle.xcor() == 350:
                    self.x_movement = speed * -1
                elif self.x_movement < 1 and paddle.xcor() == -350:
                    self.x_movement = speed

                angle = random.randint(0, 15)
                if self.y_movement > 0 and self:
                    self.y_movement = angle * -1
                else:
                    self.y_movement = angle


    def change_y_direction(self):
        self.y_movement *= -1


    def reset(self):
        self.goto(0, 0)
        if self.x_movement >= 0:
            self.x_movement = -15
        else:
            self.x_movement = 15
