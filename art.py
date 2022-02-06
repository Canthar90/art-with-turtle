
from turtle import Turtle, Screen, colormode
import random

franklin = Turtle()
franklin.shape("turtle")
franklin.speed("fastest")
colormode(255)
rgb_colors = ((245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102))

color=0
# 12  7
def draw_row(startx, starty):
    global color
    for l in range(16):
        franklin.penup()
        franklin.setposition(startx+(l*50), starty)
        # franklin.color()
        franklin.dot(20, random.choice(rgb_colors))

        color += 1


startx = -360
starty = -300
for r in range(12):
    draw_row(startx,(starty + r* 50))








screen = Screen()
screen.exitonclick()