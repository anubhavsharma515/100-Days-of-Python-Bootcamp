from turtle import Turtle
import random

class Ball(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('blue')
    self.penup()
    self.x_distance = 5
    self.y_distance = 5

  def move(self):
    new_x = self.xcor() + self.x_distance
    new_y = self.ycor() + self.y_distance
    self.goto(new_x, new_y)

  def bounce_x(self):
    self.x_distance *= -1

  def bounce_y(self):
    self.y_distance *= -1
 
