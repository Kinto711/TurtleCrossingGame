from turtle import Turtle
import random

color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130),
              (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104),
              (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170),
              (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44),
              (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]


class Blocks(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(900, 900)
        self.hideturtle()
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        ran_number_blocks = random.randint(20, 40)
        for i in range(0, ran_number_blocks):
            shape_size = random.randint(1, 3)
            ran_distance = random.randrange(20, 480, 20)
            x_cor = random.randrange(-380, 380, ran_distance)
            y_cor = random.randrange(-200, 200, 65)
            block = Turtle("square")
            # block.shape("square")
            block.shapesize(3, 1)
            block.penup()
            block.color(random.choice(color_list))
            block.setheading(90)
            block.goto(x_cor, y_cor)
            self.blocks.append(block)

    def extra_blocks(self):
        shape_size = random.randint(1, 3)
        ran_distance = random.randrange(80, 560, 40)

        x_cor = random.randrange(320, 680, ran_distance)

        y_cor = random.randrange(-200, 200, 60)

        block = Turtle("square")
        # block.shape("square")
        block.shapesize(3, 1)
        block.penup()
        block.color(random.choice(color_list))
        block.setheading(90)
        block.goto(x_cor, y_cor)

        block.goto(x_cor, y_cor)
        self.blocks.append(block)

    def move(self):
        for block in self.blocks:
            x_cor = block.xcor()
            y_cor = block.ycor()
            block.goto(x_cor - 8, y_cor)