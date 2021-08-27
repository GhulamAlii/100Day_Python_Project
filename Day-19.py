#               More About Turtle Graphic And Higher Order Function
from turtle import Turtle, Screen
import random
#               Pen Drawer

# tom = Turtle()
screen = Screen()
#
#
#
# def move_f():
#     tom.forward(20)
#
#
# def move_b():
#     tom.backward(20)
#
#
# def move_l():
#     tom.left(20)
#
#
# def move_r():
#     tom.right(20)
#
#
# def clear():
#     tom.clear()
#     tom.penup()
#     tom.home()
#     tom.pendown()
#
#
# screen.listen()
#
# screen.onkey(move_f, "w")
# screen.onkey(move_b, "s")
# screen.onkey(move_l, "a")
# screen.onkey(move_r, "d")
# screen.onkey(clear, "c")

#                   Turtle Race Game

screen.setup(width=500,height=400)
userInp = screen.textinput("User BET","Enter your winner color")
race_start = False
colors = ["red", "orange", "yellow", "green", "blue"]
turtles = []
cord_y = -120

for color in colors:

    poly = Turtle(shape="turtle")
    poly.color(color)
    poly.penup()
    poly.goto(x=-230, y=cord_y)
    cord_y = cord_y + 50
    turtles.append(poly)
if userInp:
    race_start = True

while race_start:

    for turtle in turtles:
        if turtle.xcor()>220:
            race_start = False
            winner = turtle.pencolor()
            if turtle.pencolor() == userInp:
                print(f"Congratulation! Your {winner} Turtle is Win")
                screen.clear()
            else:
                print(f"Ohh! You Lose  {winner} Turtle is Win")
                screen.clear()
        turtle.forward(random.randint(0,10))


