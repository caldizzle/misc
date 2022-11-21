# import relevant libraries
import turtle
import random

# create variable names for the turtle and the screen
window = turtle.Screen()
arthur = turtle.Turtle()

#set the window background color to purple
window.colormode(255)
window.bgcolor(50,0,70)

#set the turtle's speed
arthur.speed(0)

#set the turtle color to yellow
arthur.pencolor(255,255,0)

# define a function to draw a shape
# each time this function runs, the turtle will draw a line and turn
def shape(angle,side,limit):
    # this code will make the spiral reverse direction a couple times as it goes
    # reverseDirection = 200
    # if side % (reverseDirection*2) == 0:
    #     angle = angle + 2
    #     print(side)
    # elif side % reverseDirection == 0:
    #     angle = angle - 2
    #     print(side)


    # go forward for the side length
    arthur.forward(side)

    # turn by the specified angle
    arthur.right(angle)

    # increase the side length for the next line segment we draw
    side = side + 2

    # if the side length is still smaller than the limit we have set for it, draw another line using the same function
    # when you call a function within itself, that is called recursion
    if side < limit:
        shape(angle, side, limit)

#create variables for angle, side and limit
angle = 119
side = 0
limit = 600

#draw the shape
shape(angle, side, limit)

#preserve the drawing until the user clicks
window.exitonclick()
