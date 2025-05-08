from turtle import Turtle
from screen_pars import *
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shapesize(2)
        self.shape("circle")
        self.penup()
        self.speed = 5
        self.x_move = self.speed
        self.y_move = self.speed


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_x_pad(self, change):
        self.x_move += change
    def reset_position(self):
        self.x_move = self.speed
        self.y_move = self.speed
        self.goto(0, 0)

        bounce_rand = random.randint(0,2)
        if bounce_rand == 0:
            self.bounce_x()
        elif bounce_rand == 1:
            self.bounce_y()
        print('mowa pilka')
        print(self.x_move, self.y_move)