
import turtle

def square(bob,length): 
    for i in range(4):
        bob.forward(length)
        bob.left(90)

jn = turtle.Screen()
bob = turtle.Turtle()
length = float(input('Digite o tamanho do lado do quadrado: '))
square(bob,length)
