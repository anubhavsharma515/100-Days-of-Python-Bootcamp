from turtle import Turtle

class Player(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape('turtle')
    self.penup()
    self.seth(90)
    self.goto(0, -280)

  def f(self):
    self.forward(5)

  def reset_position(self):
    self.goto(0, -280)



