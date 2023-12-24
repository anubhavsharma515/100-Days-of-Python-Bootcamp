from turtle import Screen
from car import Car
from player import Player
from level import Level
import time
import random

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
cars = []
next_car = 30
current_level = 1
speed = 2

player = Player()
level = Level(current_level)

screen.listen()
screen.onkey(player.f, 'Up')

is_game_over = False
while not(is_game_over):
  screen.update()
  time.sleep(0.1)

  # Check if user crossed the level
  if player.ycor() > 280:
    # update scoreboard
    current_level += 1
    level.update_level(current_level)
    # move the turtle back to base
    time.sleep(2)
    player.reset_position()
    # speed up existing cars, and update starting speed for new cars
    speed += 1
    for new_car in cars: 
      new_car.update_speed(speed)

  # Deploy new car either:
  # 1. at start of game
  # 2. after the last deployed car has crossed a randomly decided distance (between 10/45 steps)
  if len(cars) == 0 or cars[-1].xcor() < (300-next_car):
    new_car = Car(starting_x=300, speed=speed)
    cars.append(new_car)
    next_car = random.randint(10, 45)
  
  # ensure all cars move together
  for new_car in cars: 
    if player.distance(new_car) < 20:
      is_game_over = True
      level.game_over()
    new_car.move()

screen.exitonclick()
