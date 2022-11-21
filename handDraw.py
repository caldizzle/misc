from turtle import *

def initializeTurtle(size):
	padding = 25  # increase if patterns gets cut off
	
	setup(width = size + padding, height = size + padding)
	
	reset() # Clear any existing turtle drawings
	# and reset turtle position & heading.
	
	pensize(1) # Choose a pen thickness
	
	speed(0) # Set the speed
	
	up()
	goto(0, 0)
	down()

def handdraw(color):
	pendown()
	ondrag(goto)

def drawAndRecord(x, y):
	


if __name__=='__main__':
	initializeTurtle(600)
	handdraw("red")
	# exitonclick()
