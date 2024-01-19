from turtle import Turtle

ALIGN = "center"
FONT = "Courier"
FONT_SIZE = 80
FONT_WEIGHT = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=(FONT, FONT_SIZE, FONT_WEIGHT))
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=(FONT, FONT_SIZE, FONT_WEIGHT))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()