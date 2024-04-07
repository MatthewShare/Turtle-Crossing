from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.write(f"Level {self.level}", font=FONT)

    def level_up_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(-100, 0)
        self.write(f"Game Over", font=FONT)




