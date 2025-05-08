
from turtle import Screen, Turtle
from tkinter import messagebox
from game import Game
from detection import *
from blocks_gen import get_blocks
from screen_pars import *
from results import *

import time

#pyinstaller --icon=icon.ico  --windowed Breakout.py


def toggle_pause():
    global game_paused
    game_paused = not game_paused
    if game_paused:
        display_pause_message()
    else:
        clear_pause_message()

def display_pause_message():
    pause_message.clear()
    pause_message.write("GAME PAUSED, PRESS SPACE TO CONTINUE", align="center", font=("Courier", 22, "normal"))


def clear_pause_message():
    pause_message.clear()

def restart_game():
    global game, game_paused

    # Clear the screen
    screen.clear()

    # Re-setup the screen
    screen.bgcolor("black")
    screen.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
    screen.title("Breakout")
    screen.tracer(0)

    # Re-create the game
    game = Game()

    frame()

    # Reset the screen event listeners
    screen.listen()
    screen.onkeypress(game.paddle.go_right, "Right")
    screen.onkeypress(game.paddle.go_left, "Left")
    screen.onkeypress(toggle_pause, "space")
    toggle_pause()


def frame():

    if not game_paused:
        screen.update()
        game.ball.move()

        #Detect collision with ceiling
        detect_celling_bounce(game.ball)

        # Detect collision with side walls
        detect_sidewall_bounce(game.ball)

        # Detect lose of chance
        detect_chance_lose(game.scoreboard,game.ball)

        #Detect paddle bounce:
        detect_paddle_bounce(game.paddle, game.ball)

        # Detect block collision:
        if game.ball.ycor() > 0:
            for index, block in enumerate(game.blocks):
                detect_block_collision(block, game.ball, game.scoreboard)





        # Check if level completed:
        if game.scoreboard.score == game.points_to_get:
            if game.scoreboard.level < 3:
                game.scoreboard.level_up()
                time.sleep(1)
                game.ball.speed += 2
                print(f'speed: {game.ball.speed}')
                game.ball.reset_position()
                get_blocks(game)

            else:
                game.game_is_on = False

                messagebox.showinfo(title="Gratulacje", message=f'Ukończyłeś grę!\nUzyskałeś maksymalną liczbę '
                                                                    f'punktów.{text_make(game.scoreboard.score)}')

        # Check if game over:
        if game.scoreboard.life > 0 and game.game_is_on:
            screen.ontimer(frame, FRAME_RATE_MS)
        elif game.scoreboard.life < 1:
            game.game_is_on = False

            messagebox.showinfo(title="Koniec gry", message=f"Straciłeś wszystkie szanse.{text_make(game.scoreboard.score)}", )
            restart_game()
    else:
        screen.ontimer(frame, FRAME_RATE_MS)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
screen.title("Breakout")
screen.tracer(0)
game = Game()

# Variable to track paused state
game_paused = False


# Set window icon
turtle_screen = screen.getcanvas().winfo_toplevel()
turtle_screen.iconbitmap("icon.ico")

screen.listen()
screen.onkeypress(game.paddle.go_right, "Right")
screen.onkeypress(game.paddle.go_left, "Left")
screen.onkeypress(toggle_pause, "space")

# Create a turtle for displaying the pause message
pause_message = Turtle()
pause_message.hideturtle()
pause_message.penup()
pause_message.color("white")
pause_message.goto(0, -200)


frame()
toggle_pause()


screen.exitonclick()
