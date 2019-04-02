import turtle

def square(bob): 
    for i in range(4):
        bob.forward(50)
        bob.left(90)

jn = turtle.Screen()
bob = turtle.Turtle()
square(bob)

# chamar a varial t de bob, depois
