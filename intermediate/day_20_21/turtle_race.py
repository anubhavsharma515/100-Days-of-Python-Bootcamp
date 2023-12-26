from turtle import Turtle, Screen
import random


is_race_on = False
# Initializes a screen
screen = Screen()
# Presents the screen with the assigned dimensions
screen.setup(width=500, height=500)
finish_line = screen.window_width() / 2


# Title is top of the box, prompt is like `input`
user_bet = screen.textinput(title='Which turtle do you bet will win the race?', prompt='Choose a color: ')
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
  # Simply creates a single cursor
  new_turtle = Turtle(shape='turtle')
  # Sets the color of the cursor
  new_turtle.color(colors[turtle_index])
  # Lifts up the pen to stop tracking the points between old and new position
  new_turtle.penup()
  # Sends the turtle from origin to a particular y (but along the same starting line)
  # -ve x is likely because of origin being 0
  new_turtle.goto(x=-230, y=y_position[turtle_index])
  all_turtles.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)
    
    if turtle.xcor() >= finish_line:
      is_race_on = False
      
  
# Persists the screen until a user clicks
screen.exitonclick()
