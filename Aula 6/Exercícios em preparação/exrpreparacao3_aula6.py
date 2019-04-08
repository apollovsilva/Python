import turtle

def polygon(bob,length,n): 
    for i in range(n):
        bob.forward(length)
        bob.left(360/n)

jn = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")

length = float(input('Digite o tamanho do lado do polígono: '))
lados = int(input('Digite o número de lados do polígono: '))

polygon(bob,length,lados)
