from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)
snake = Turtle()

start = True

def f():
  snake.forward(2)

def l():
  current_angle = snake.heading()
  if current_angle in (90, 270): 
    snake.seth(180)
    
def r():
  current_angle = snake.heading()
  if current_angle in (90, 270): 
    snake.seth(0)

def u():
  current_angle = snake.heading()
  if current_angle in (0, 180): 
    snake.seth(90)

def d():
  current_angle = snake.heading()
  if current_angle in (0, 180): 
    snake.seth(270)

screen.listen()

screen.onkey(r, "Right")
screen.onkey(l, "Left")
screen.onkey(u, "Up")
screen.onkey(d, "Down")

while start:
  if (abs(snake.xcor()) > screen.window_width() / 2) or (abs(snake.ycor()) > screen.window_height() / 2):
    start = False
  else:
    f()
  
screen.exitonclick()
