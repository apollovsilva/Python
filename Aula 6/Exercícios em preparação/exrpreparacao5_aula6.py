import turtle
import math

def polyline(t, length, n, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n): 
    angle = 360/n # ângulos externos de um polígono regular de n lados
    polilyne(t, length, n, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360 
    n = int(arc_length / 3) + 1 
    step_length = arc_length / n 
    step_angle = float(angle) / n 
    polyline(t, step_length, n, step_angle)

def circle(t,r):
    arc(t, r, 360) # coloquei 360 pois quero de desenhe sempre um círculo

jn = turtle.Screen()
bob = turtle.Turtle()

r = float(input('Digite o valor do raio: '))

circle(bob,r)
