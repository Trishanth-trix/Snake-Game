from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0
        with open("high_score.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,290)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.score+=1
        self.update_score()
    def reset(self):

        if(self.high_score<=self.score):
            self.high_score=self.score
            with open("high_score.txt", mode="w")as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center",font=("Arial", 24, "normal"))
        self.high_score=self.score





