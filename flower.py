import turtle
import math

def polyline(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360 
    n = int(arc_length / 3) + 1 
    step_length = arc_length / n 
    step_angle = float(angle) / n 
    polyline(t, step_length, n, step_angle)


def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


#def move(t, length):
 #   """Move Turtle (t) forward (length) units without leaving a trail.
  #  Leaves the pen down.
   # """
    #t.pu()
    #t.fd(length)
    #t.pd()

#desenhando o talo e folha

def talo(t):
    t.pensize(3)
    t.color("brown")
    t.rt(90)
    t.fd(150)
    t.pu()
    t.lt(180)
    t.fd(45)
    t.pd()
    t.rt(60)
    t.color("green","green")
    t.begin_fill()
    petal(bob,60.0,60.0)
    t.end_fill()
    
    
    
    
    

bob = turtle.Turtle()
#bob.color("green")
bob.speed(0)

flower(bob, 7, 60.0, 60.0)
talo(bob)

#Para salvar o desenho da tela num arquivo .ps   
tc= turtle.Screen().getcanvas()
tc.postscript(file="flores.ps")
