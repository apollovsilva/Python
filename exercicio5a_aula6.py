import turtle
c = input('Digite a cor do fundo da tela desejada: ')
t = input('Digite o nome da tela desejado: ')

jn = turtle.Screen()
jn.title(t)
jn.bgcolor(c)


#x = input('Digite a cor deseja para a linha: ')
#y = float(input('Digite o tamanho da caneta desejado: '))

teca = turtle.Turtle()
teca.color("blue")
teca.pensize(2)
teca.shape("turtle")
teca.speed(1)

#teca.left(144)
#teca.forward(100)

for i in range(5):
    teca.right(144)
    teca.forward(100)
