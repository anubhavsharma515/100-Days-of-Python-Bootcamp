from turtle import Screen
import time
import random

from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

start = True
food_found = False

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.r, "Right")
screen.onkey(snake.l, "Left")
screen.onkey(snake.u, "Up")
screen.onkey(snake.d, "Down")

while start:
  if not(snake.crossed_boundary()):
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
      food.refresh()
      snake.update()
      food.ht()
      food = Food()
  else:
    start = False
    

screen.exitonclick()
