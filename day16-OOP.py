#                          TURTLE GRAPHIC

# from turtle import Turtle, Screen
#
# tom = Turtle()
# tom.shape("turtle")
# tom.color("green")
# tom.forward(100)
# on_screen = Screen()
# on_screen.exitonclick()

#                        PRETTY TABLE

from prettytable import PrettyTable

table = PrettyTable()
table.field_names=["Name","Age"]
table.add_row(["Ali","20"])
table.add_row(["Alishba","21"])
table.add_row(["Iman","1"])
table.align="l"
print(table)