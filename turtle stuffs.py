import turtle
scn = turtle.Screen()
t = turtle.Turtle()

width, height = scn.screensize()

t.penup()
t.goto(-200, 150)
t.pendown()

def draw_line(size):
	t.right(90)
	t.forward(size)
	t.right(180)
	t.forward(size)

def no_trace(distance):
	t.right(90)
	t.penup()
	t.forward(distance)
	t.pendown()

for i in range(1,20):
	draw_line(width)
	no_trace(i*10)

scn.exitonclick()
