import turtle

scn = turtle.Screen()
t = turtle.Turtle()

def shrub(trunkLength, angle, shrinkFactor, minLength):
    """
    Draws a shrub as specified in Lab 9 Task 4.
    Returns a pair (a 2-tuple) consisting of
      (1) the total number of branches (including the trunk) and
      (2) the total length of the branches (including the trunk)
    of the shrub.
    Assume that the turtle is positioned at the base of the main
    trunk facing north before this function is called.
    """
    if trunkLength < minLength:
        # base case
        pass
    else:
        #draw the trunk
        t.fd(trunkLength)
        #setup to draw left branch
        t.lt(angle)
        #draw the left branch
        leftN, leftLen = shrub(trunkLength*shrinkFactor*shrinkFactor, angle, shrinkFactor, minLength)
        #setup to draw right branch
        t.rt(angle*2)
        #draw the right branch
        rightN, rightLen = shrub(trunkLength*shrinkFactor, angle, shrinkFactor, minLength)
        #maintain invariance
        t.lt(angle); t.bk(trunkLength)
        #return the tuple n,l

t.penup()
t.goto(-200,-200)
t.lt(90)
t.pendown()
shrub(200, 30, 0.75, 40)

scn.exitonclick()
