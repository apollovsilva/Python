import turtle
import math

def polygon(t,l,n): 
    for i in range(n):
        t.forward(l)
        t.left(360/n)

def circle(t,r):
    circunf = 2*math.pi*r
    n = int((circunf/3) + 3)
    length = circunf/n
    polygon(t,length,n)

jn = turtle.Screen()
bob = turtle.Turtle()

r = float(input('Digite o valor do raio: '))

circle(bob,r)
