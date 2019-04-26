class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancia_de_origem(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def reflexao_x(self):
        return Ponto(- self.x, self.y)

    def inclinacao_da_origem(self, alvo):
        m = (alvo.y - self.y)/(alvo.x - self.x)
        return m

    def parametros_reta(self, alvo):
        a = (alvo.y - self.y)/(alvo.x - self.x)
        b = (self.y * alvo.x - self.x * alvo.y)/(alvo.x - self.x)
        return Ponto(a, b)


    
def ponto_medio(p1, p2):
        mx = (p1.x + p2.x)/2
        my = (p1.y + p2.y)/2
        return Ponto(mx, my)

    

p = Ponto()
q = Ponto()
r = Ponto(0,0)

p.x = float(input('Digite a coordenada x do ponto inicial: '))
p.y = float(input('Digite a coordenada y do ponto inicial: '))
q.x = float(input('Digite a coordenada x do ponto final: '))
q.y = float(input('Digite a coordenada y do ponto final: '))

print('Ponto médio: ', ponto_medio(p, q))

print('Refelxão da componente x do 1° ponto: ', p.reflexao_x())

#print('Inclinação da origem para 1ª coordenada digitada: ', r.inclinacao_da_origem(p))

#print('Inclinação da origem para 2ª coordenada digitada: ', r.inclinacao_da_origem(q))

# no EXR 3, o método inclinacao_da_origem necessita de um argmento. Logo se fizermos como pedido ao compilar dará um erro por escrever simplesmente p.inclinacao_da_origem() sem por o argumento no método

#print('Parêmtros a e b para equação da reta: ', p.parametros_reta(q))

#os dois últimos métodos falham se a tivermos uma função linear (b = 0) 

if p.x == 0 and q.x == 0 :
    print('Sua reta é uma reta vertical')
elif p.x == 0 and p.y == 0:
    a = q.y / q.x
    print('Sua reta passa pela origem. O coeficiente angular é: ', a)
else:
    print('Inclinação da origem para 1ª coordenada digitada: ', r.inclinacao_da_origem(p))
    print('Inclinação da origem para 2ª coordenada digitada: ', r.inclinacao_da_origem(q))
    print('Parêmtros a e b para equação da reta: ', p.parametros_reta(q))
