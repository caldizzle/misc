from turtle import *

def drawTriangle(sideLen):
    pd()
    fd(sideLen)
    lt(120)
    fd(sideLen)
    lt(120)
    fd(sideLen)
    lt(120)
    pu()

def initializeTurtle(sideLen):
    """initialize turtle to bottom left end point of
    outer triangle facing east"""
    setup(sideLen+100, sideLen+100) # Create a turtle window
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(2) # Choose a pen thickness
    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal
    pu()
    setx(-sideLen/2) # initial position x coordinate
    sety(-sideLen/2) # initial position y coordinate


def sierpinski(sideLen, level):
    if level == 0:
        pass
    else:
        # draw outerbig triangle first
        drawTriangle(sideLen)
        # position to draw upper subpattern
        lt(60); fd(sideLen/2); rt(60)
        # draw upper subpattern
        sierpinski(sideLen/2, level-1)
        # return to draw lower-left subpattern
        lt(60); bk(sideLen/2); rt(60)
        # draw lower left subpattern
        sierpinski(sideLen/2, level-1)
        # position to draw lower-right subpattern
        fd(sideLen/2)
        sierpinski(sideLen/2, level-1)
        # return to original position
        bk(sideLen/2)


def testSierpinski(sideLen, level):
    initializeTurtle(sideLen)
    sierpinski(sideLen, level)
    getscreen().getcanvas().postscript(file="sierpinski-{}-{}.eps".format(sideLen, level))


if __name__ == '__main__':
    """Test calls"""
    #testSierpinski(600, 0)
    #testSierpinski(600, 1)
    #testSierpinski(600, 2)
    #testSierpinski(600, 3)
    #testSierpinski(600, 4)
    #testSierpinski(600, 5)
    testSierpinski(600, 6)
    #testSierpinski(600, 7)
