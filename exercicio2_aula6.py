import turtle
c = input('Digite a cor do fundo da tela desejada: ')
t = input('Digite o nome da tela desejado: ')

jn = turtle.Screen()
jn.title(t)
jn.bgcolor(c)


x = input('Digite a cor deseja para a linha: ')
y = float(input('Digite o tamanho da caneta desejado: '))

teca = turtle.Turtle()
teca.color(x)
teca.pensize(y)

for i in range(4):
    teca.forward(100)
    teca.left(90)
