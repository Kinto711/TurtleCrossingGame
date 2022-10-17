from turtle import Turtle



class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.goto(0, -240)
        self.setheading(90)



    def up(self):
        self.forward(20)

    # def down(self):
    #     self.forward(-20)

    def left(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.setheading(90)
        self.goto(x_cor -20, y_cor)

    def right(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.setheading(90)
        self.goto(x_cor + 20, y_cor)

    def reset_position(self):
        self.goto(0, -240)