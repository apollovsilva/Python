import turtle
#c = input('Digite a cor do fundo da tela desejada: ')
#t = input('Digite o nome da tela desejado: ')

jn = turtle.Screen()
jn.title("Olá")
jn.bgcolor("lightgreen")


#x = input('Digite a cor deseja para a linha: ')
#y = float(input('Digite o tamanho da caneta desejado: '))

teca = turtle.Turtle()
teca.color("blue")
teca.pensize(2)
teca.shape("turtle")
teca.speed(3)

teca.penup()
teca.backward(500)
teca.pendown()

for j in range(4):
    teca.penup()
    teca.forward(200)
    teca.pendown()
    for i in range(5):
        teca.right(144)
        teca.forward(100)

