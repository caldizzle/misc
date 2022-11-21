import turtle

# create variable names for the turtle and the screen
window = turtle.Screen()
arthur = turtle.Turtle()

#set the window background color to purple
window.colormode(255)
window.bgcolor("black")

#set the turtle's speed
arthur.speed(0)

#set the turtle color to yellow
arthur.pencolor(255,255,0)

#create variables for angle, side and limit
angle = (360/3) + 1
side = 0
limit = 600

while side < limit:

    arthur.penup()

    # go forward for the side length
    arthur.forward(side)

    arthur.pendown()

    # turn by the specified angle
    arthur.right(angle)

    # increase the side length for the next line segment we draw
    side = side + 2

    arthur.circle(side)

#preserve the drawing until the user clicks
window.exitonclick()
