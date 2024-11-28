from turtle import Turtle
from paddle import Paddle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Player(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.penup()
        self.score = 0
        self.paddle = Paddle(xcor)
        self.hideturtle()
        self.color("white")
        if xcor > 0:
            self.goto(200, 260)
        else:
            self.goto(-200, 260)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()
