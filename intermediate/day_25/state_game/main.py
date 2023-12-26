from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title('US States Game')
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

states = pd.read_csv('50_states.csv')
# Get # of states
total_states = states.shape[0]
number_guessed = 0
states_guessed = []
start_game = True

while start_game: 
    state_name = screen.textinput(title=f'Enter a state name (Guessed {number_guessed} / {total_states})', prompt='name')
    if state_name in states.state.values and state_name not in states_guessed:
        number_guessed += 1
        states_guessed.append(state_name)
        details = states.loc[states.state == state_name]
        state_x = int(details.x)
        state_y = int(details.y)
        new_turtle = Turtle()
        new_turtle.ht()
        new_turtle.penup()
        new_turtle.goto(state_x, state_y)
        new_turtle.write(arg=f'{state_name}', move=False, align='center', font=('Arial', 10, 'normal'))

screen.exitonclick()

