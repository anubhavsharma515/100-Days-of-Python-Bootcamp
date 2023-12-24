from turtle import Turtle
import random

class Car(Turtle):
  
  COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
  
  def __init__(self, starting_x, speed):
    super().__init__()
    self.shape("square")
    self.color(self.COLORS[random.randint(0, 5)])
    self.penup()
    self.shapesize(stretch_wid=1, stretch_len=2)
    self.moving_speed=speed
    self.place_car(starting_x)
  
  def move(self):
    self.backward(self.moving_speed)
  
  def place_car(self, start):
    self.goto(start, random.randint(-start, start))

  def update_speed(self, speed):
    self.moving_speed = speed
    
