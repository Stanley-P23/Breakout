from turtle import Turtle
from screen_pars import *


class Block(Turtle):

    def __init__(self, row, position, size):
        super().__init__()
        self.size = size
        self.shape("square")
        self.row = row
        self.colors = ['#FFDEB9', '#FC2947', '#7149C6']

        self.color(self.colors[self.row])
        self.shapesize(stretch_wid=4, stretch_len=size)
        self.penup()
        self.goto(position)
        self.hidden = 0



