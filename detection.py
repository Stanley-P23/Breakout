from screen_pars import *
import time



def collided(block, scoreboard):
    block.undo()
    block.goto(0, 3000)
    scoreboard.score_add()
    print('block collision')
    
def detect_block_collision(block, ball, scoreboard):


    # Lower wall
    if block.xcor() - 10 * block.size - 20 < ball.xcor() < block.xcor() + 10 * block.size + 20 and abs(
             block.ycor() - ball.ycor() - 60) <= 6:

        if ball.y_move > 0:
            ball.bounce_y()
            collided(block, scoreboard)


    # Upper wall
    if block.xcor() - 10 * block.size - 20 < ball.xcor() < block.xcor() + 10 * block.size + 20 and abs(
            ball.ycor() - block.ycor() - 60) <= 6:

        if ball.y_move < 0:
            ball.bounce_y()
            collided(block, scoreboard)

    # Left wall
    if block.ycor() - 40 - 20 < ball.ycor() < block.ycor() + 40 + 20 and abs(
            block.xcor() - ball.xcor() - 20 - 10*block.size) <= 6:

        if ball.x_move > 0:
            ball.bounce_x()
            collided(block, scoreboard)

    # Right wall
    if block.ycor() - 40 - 20 < ball.ycor() < block.ycor() + 40 + 20 and abs(
            ball.xcor() - block.xcor() - 20 - 10*block.size) <= 6:

        if ball.x_move < 0:
            ball.bounce_x()
            collided(block, scoreboard)  
            
def detect_paddle_bounce(paddle, ball):

    if paddle.xcor() - 240 < ball.xcor() < paddle.xcor() + 240 and abs(
            ball.ycor() - paddle.ycor() - 20) <= 6:
        ball.bounce_y()
        ball.bounce_x_pad((ball.xcor() - paddle.xcor()) / 220 * 3.5)

        print('paddle collision')
        print(f'Change: {(ball.xcor() - paddle.xcor()) / 220 * 3.5}')

def detect_chance_lose(scoreboard, ball):
    if ball.ycor() < -WIN_HEIGHT / 2:
        print('you lose')
        if scoreboard.life > 1:
            time.sleep(1)
        ball.reset_position()
        scoreboard.life_lose()

def detect_sidewall_bounce(ball):
    if ball.xcor() > WIN_WIDTH / 2 - 20 or ball.xcor() < -WIN_WIDTH / 2 + 20:
        ball.bounce_x()
        print('sidewall collision')
        
def detect_celling_bounce(ball):
    if ball.ycor() > WIN_HEIGHT/2 - 10:
        ball.bounce_y()
        print('ceiling collision')