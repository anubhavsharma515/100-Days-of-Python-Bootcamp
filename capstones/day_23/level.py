from turtle import Turtle

class Level(Turtle):

  def __init__(self, level):
    super().__init__()
    self.penup()
    self.ht()
    self.goto(-200, 200)
    self.update_level(level)

  def update_level(self, level):
    self.clear_level()
    self.level = level
    self.write(f"Level = {level}", False, align="left", font=("Courier", 20, "normal"))

  def clear_level(self):
    self.clear()

  def game_over(self):
    self.goto(0, 0)
    self.write("Game Over.", False, align="center", font=("Courier", 20, "normal"))
    
