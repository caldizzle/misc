# draw a recursive fern or tree
import turtle

scn = turtle.Screen()
t = turtle.Turtle()

t.penup()
t.speed(0)
t.goto(0, -200)
t.left(90)

scaleFactor = 0.8
angle = 57

def recursiveFern(layers, size):
    # base case
    if layers == 0:
        pass
    else:
        # draw a smaller recursiveFern
        t.pendown()
        t.forward(size)
        t.right(angle)
        recursiveFern(layers - 1, size * scaleFactor)
        t.left(angle * 2)
        recursiveFern(layers - 1, size * scaleFactor)
        t.right(angle)
        t.backward(size)


recursiveFern(12, 150)

scn.exitonclick()
