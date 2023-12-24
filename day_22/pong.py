from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title('pong')
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)

top_paddle = Paddle('top')
bottom_paddle = Paddle('bottom')
ball = Ball() 

top_score = 0
bottom_score = 0

screen.listen()
screen.onkey(bottom_paddle.l, 'Left')
screen.onkey(bottom_paddle.r, 'Right')
screen.onkey(top_paddle.l, 'a')
screen.onkey(top_paddle.r, 'd')

game_is_on = True
while game_is_on:
  time.sleep(0.09)
  screen.update()
  ball.move()
  if ball.xcor() > 270 or ball.xcor() < -270:
    ball.bounce_x()
  elif ball.distance(top_paddle.paddle.pos()) < 50 and ball.ycor() > 250 or ball.distance(bottom_paddle.paddle.pos()) < 50 and ball.ycor() < -250:
    ball.bounce_y()
  elif ball.ycor() > 290 or ball.ycor() < -290:
    print("OOB")
    ball.home()


screen.exitonclick()
