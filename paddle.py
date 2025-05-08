from turtle import Turtle
from screen_pars import *

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#FE6244")
        self.shapesize(stretch_wid=1, stretch_len=22)
        self.penup()
        self.goto(position)
        self.step = STEP

    def go_left(self):
        if self.xcor() - self.shapesize()[1]*5 > -WIN_WIDTH/2:
            self.bk(self.step)

    def go_right(self):
        if self.xcor() + self.shapesize()[1] * 5 < WIN_WIDTH / 2:
            self.fd(self.step)
