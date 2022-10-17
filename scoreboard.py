

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.create_banner()

    def create_banner(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-250, 260)
        self.write(f"Level: {self.level}", False, align="center", font=('Arial', 25, 'normal'))

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align="center", font=('Arial', 25, 'normal'))
        print("+1 to score")
        print(self.level)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 60, 'normal'))