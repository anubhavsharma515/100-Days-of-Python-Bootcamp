from turtle import Turtle

class Paddle():

  TOP_PADDLE_Y = 280 
  BOTTOM_PADDLE_Y = -280
  MOVING_DISTANCE = 20

  def __init__(self, orientation):
    self.paddle = Turtle()
    self.paddle.shape('square')
    self.paddle.color('white')
    self.paddle.penup()
    self.paddle.shapesize(stretch_len=5, stretch_wid=1)
    self.place_paddle(orientation)
  
  def place_paddle(self, orientation):
    self.paddle.goto(0, self.TOP_PADDLE_Y if orientation == 'top' else self.BOTTOM_PADDLE_Y)

  def l(self):
    if self.paddle.xcor() > -240:
      new_x = self.paddle.xcor() - self.MOVING_DISTANCE
      self.paddle.goto(new_x, self.paddle.ycor())

  def r(self):
    if self.paddle.xcor() < 240:
      new_x = self.paddle.xcor() + self.MOVING_DISTANCE
      self.paddle.goto(new_x, self.paddle.ycor())

