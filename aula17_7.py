import turtle
from retangulo import *

def desenhar_ret(t, r):
    t.pu()                # Levana a caneta
    t.goto(r.p.x, r.p.y)  # Define a posição da tartaruga
    #print(t.position())

    t.pd()                # Abaixa a caneta
    t.fd(r.l)             # Largura do retângulo
    t.lt(90)              # Gira um ângulo de 90º
    t.fd(r.h)             # Altura do retângulo
    t.lt(90)
    t.fd(r.l)
    t.lt(90)
    t.fd(r.h)

jn = turtle.Screen()      # Configura a janela e seus atribtos
jn.bgcolor("white")       # Define a cor do fundo da janela
jn.title("Retângulo")     # Define o título da janela

bob = turtle.Turtle()
bob.shape("turtle")
bob.pensize(3)
#bob.speed("fastest")

p = Ponto(40,40)

r = Retangulo(100, 50, p)

desenhar_ret(bob, r)
