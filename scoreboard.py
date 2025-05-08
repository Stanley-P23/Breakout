from turtle import Turtle
from screen_pars import *

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.life = 3
        self.score = 0
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        #LIFE
        self.goto(-WIN_WIDTH/2+60, WIN_HEIGHT/2-50)
        self.write('LIFE ', align="left", font=("Courier", 22, "normal"))

        self.goto(-WIN_WIDTH / 2 + 190, WIN_HEIGHT / 2 - 50)
        self.write(self.life, align="left", font=("Courier", 22, "normal"))

        #SCORE
        self.goto(-WIN_WIDTH/2+60, WIN_HEIGHT/2 - 100)
        self.write('SCORE', align="left", font=("Courier", 22, "normal"))

        self.goto(-WIN_WIDTH / 2 + 190, WIN_HEIGHT / 2 - 100)
        self.write(self.score, align="left", font=("Courier", 22, "normal"))

        # LEVEL
        self.goto(WIN_WIDTH / 2 - 190, WIN_HEIGHT / 2 - 50)
        self.write('LEVEL', align="left", font=("Courier", 22, "normal"))

        self.goto(WIN_WIDTH / 2 - 60, WIN_HEIGHT / 2 - 50)
        self.write(self.level, align="left", font=("Courier", 22, "normal"))

    def score_add(self):
        self.score += 1
        self.update_scoreboard()

    def life_lose(self):
        self.life -= 1
        self.update_scoreboard()

    def level_up(self):
        self.life += 1
        self.level += 1
        self.update_scoreboard()
