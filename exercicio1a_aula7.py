import turtle
def draw_bar(t, height, classe):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(classe)           # classe do histograma - intervalo
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    #t.forward(10)           # tira os espaços entre as barras

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)
tess.speed(1)

#xs = [48,117,200,240,160,260,220]    # lista com as frequências
classe = float(input('Digite o intervalo do histograma (classe): '))
n = int(input('Digite a quantidade de intervalos (classes): '))
lista = []

for i in range(n):
    bin(i) = int(input('Digite o valor da frequência: '))
    lista.append(bin(i))

for a in xs:
    draw_bar(tess, a, classe)

#wn.mainloop()
