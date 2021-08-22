from turtle import Turtle, Screen, colormode
import random
import colorgram
tom = Turtle()
screen = Screen()

tom.shape("arrow")

#                               CREATE SQUARE
# for i in range(0,10):
#     tom.pu()
#     tom.forward(10)
#     tom.pd()
#     tom.forward(10)
#


#               CREATE SHAPES
# side = 3
# while (side < 11):
#     angle = 360/side
#     for i in range(side):
#         tom.forward(100)
#         tom.right(angle)
#     colormode(255)
#     tom.pencolor(random.randint(10,255),random.randint(10,255),random.randint(10,255))
#     side+=1

#                  Random Walk
# for _ in range(100):
#     colormode(255)
#     tom.pen(pencolor=(random.randint(1, 255), random.randint(1, 255), random.randint(1,255)),pensize=20)
#     tom.setx(random.randint(0,500))
#     tom.sety(random.randint(0,500))


#                   Draw A Spirograph
# tom.speed("fastest")
# def draw_shape(no_of_gap):
#     for i in range(int(360/no_of_gap)):
#         colormode(255)
#         tom.pen(pencolor=(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
#         tom.circle(100)
#         tom.setheading(tom.heading()+no_of_gap)
#
# draw_shape(10)

#                               Draw Million Dollar Dot PAnting
#                                    Extract Color on image
# rgb_color =[]
# colors = colorgram.extract("res/dot.png", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_var = (r,g,b)
#     rgb_color.append(color_var)
# print(rgb_color)

#                             Working on painting With Extracted Color

color_pal = colors = [(20, 8, 3), (200, 154, 115), (150, 80, 46), (68, 105, 142), (186, 150, 25), (220, 4, 4), (24, 216, 30), (112, 172, 116), (128, 155, 194), (200, 146, 166), (206, 26, 192), (238, 230, 56), (205, 222, 241), (207, 61, 73), (53, 30, 49), (34, 127, 34), (236, 235, 2), (89, 84, 16), (225, 78, 60), (20, 15, 214), (11, 29, 60), (39, 25, 248), (149, 6, 119), (239, 217, 231), (237, 164, 154), (165, 163, 238), (10, 97, 10), (108, 97, 230)]
colormode(255)

tom.penup()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
dots = 10

for i in range(dots):
    tom.dot(20, random.choice(color_pal))
    tom.forward(50)
    if dots % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)







screen.exitonclick()