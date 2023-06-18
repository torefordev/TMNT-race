from turtle import Turtle, Screen
from random import randint

colors = ["blue","purple","red","orange"]
turtles = []
is_racing = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet =screen.textinput(title="Make your bet", prompt="Choose a teenage mutant ninja turtle color: ")

start_x = -240
start_y = -75

for i in range(4):
    leo = Turtle("turtle") # leo is for leonardo from TMNT
    leo.color(colors[i])
    leo.up()
    leo.goto(start_x,start_y)
    start_y += 50
    turtles.append(leo)

if user_bet:
    is_racing = True

while is_racing:
    for turtle in turtles:
        random_distance = randint(1, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            is_racing = False
            winning_color = turtle.pencolor().title()
            if winning_color == user_bet:
                print(f"You Won! {winning_color} turtle wins.")
            else:
                print(f"You Lose! {winning_color} turtle wins.")




screen.exitonclick()