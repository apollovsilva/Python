import turtle
from circulo import *

def desenhar_circulo(t, circ):
    t.pu()
    #t.setx(circ.p.x)    # Define a coordenada x do cenro do circulo
    #t.sety(circ.p.y)    # Define a coordenada y do contro do circulo
    t.goto(circ.p.x, circ.p.y)
    t.fd(circ.r)        # Anda o valor do raio
    t.lt(90)
    t.pd()
    t.circle(circ.r)    # Desenha o círculo


jn = turtle.Screen()      # Configura a janela e seus atribtos
jn.bgcolor("white")       # Define a cor do fundo da janela
jn.title("Círculo")     # Define o título da janela

bob = turtle.Turtle()
bob.shape("turtle")
bob.pensize(2)
#bob.speed("fastest")

p = Ponto(40,40)

circ = Circulo(50, p)

desenhar_circulo(bob, circ)
