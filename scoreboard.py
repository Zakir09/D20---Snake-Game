from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=("Courier", 12, "normal"), align="center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.track_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", font=("Courier", 15, "normal"), align="center")

    def increase_score(self):
        self.score += 1
        self.track_score()
