class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancia_de_origem(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def reflexao_x(self):
        return Ponto(self.x, -self.y)

    def inclinacao_da_origem(self):
        m = self.y/self.x
        return m

    def parametros_reta(self, alvo):
        a = (self.y - alvo.y)/(self.x - alvo.x)
        b = (self.y * alvo.x - self.x * alvo.y)/(alvo.x - self.x)
        return Ponto(a, b)


    
def ponto_medio(p1, p2):
        mx = (p1.x + p2.x)/2
        my = (p1.y + p2.y)/2
        return Ponto(mx, my)

    

p = Ponto()
q = Ponto()
#r = Ponto(0,0)

p.x = float(input('Digite a coordenada x do ponto inicial: '))
p.y = float(input('Digite a coordenada y do ponto inicial: '))
q.x = float(input('Digite a coordenada x do ponto final: '))
q.y = float(input('Digite a coordenada y do ponto final: '))

print('Ponto médio: ', ponto_medio(p, q))

print('Reflexão da componente x do 1° ponto: ', p.reflexao_x())
print('Reflexão da componente x do 2° ponto: ', q.reflexao_x())

if p.x == 0:
   print('Seu ponto inicil forma uma reta vertical')
else:
    print('Inclinação da reta que une a origem ao 1º ponto: ', p.inclinacao_da_origem())
    
if q.x == 0:
    print('Seu ponto final forma uma reta vertical')
else:
    print('Inclinação da reta que une a origem ao 2ª ponto: ', q.inclinacao_da_origem())

if (p.x - q.x) == 0 and p.y != q.y:
    print('Reta vertical')
elif p.x == q.x and p.y == q.y:
    print('ponto')
else:    
    print('Parêmtros a e b para equação da reta: ', p.parametros_reta(q))

#if p.x == q.x and p.y == q.y:
#    print('pont')
#else:
#    print('Parêmtros a e b para equação da reta: ', p.parametros_reta(q))

