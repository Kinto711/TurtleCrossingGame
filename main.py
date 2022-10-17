from turtle import Turtle, Screen
from object import Object
from blocks import Blocks
import time
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)

set_time = 0.1


screen.bgcolor("white")
screen.setup(600, 600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)

player = Object()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")
# screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

is_on = True
blocks = Blocks()

while is_on:
    screen.update()
    time.sleep(set_time)
    blocks.extra_blocks()
    blocks.move()

    # detect collision with blocks
    for block in blocks.blocks:
        if player.distance(block) < 20:

            player.reset_position()

    # detect if player crossed the finish line
    if player.ycor() > 180:
        set_time -= 0.01
        player.reset_position()
        scoreboard.update()
        print(set_time)

screen.exitonclick()