from scoreboard import *
from paddle import Paddle
from ball import Ball
from blocks_gen import *

class Game:

    def __init__(self):
        self.levels = 3
        self.block_sizes = []
        self.x_cors = []
        self.y_cors = []
        self.rows = 3
        self.blocks = []

        self.ball = Ball()
        self.paddle = Paddle((PADDLE_X, PADDLE_Y))
        self.scoreboard = Scoreboard()
        self.game_is_on = True
        self.points_to_get = 0


        #gettig random blocks widths
        get_blocks(self)


