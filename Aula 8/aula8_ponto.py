class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancia_de_origem(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distancia_dois_pontos(self, alvo):
        """ Calcula a distancia entre dois pontos """
        return (((self.x - alvo.x) ** 2) + ((self.y - alvo.y) ** 2)) ** 0.5

    def ponto_medio(self, alvo):
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto(mx, my)

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


    

    

p = Ponto()
q = Ponto()
#r = Ponto(0,0)

p.x = float(input('Digite a coordenada x do ponto inicial: '))
p.y = float(input('Digite a coordenada y do ponto inicial: '))
q.x = float(input('Digite a coordenada x do ponto final: '))
q.y = float(input('Digite a coordenada y do ponto final: '))

print('Ponto médio: ', p.ponto_medio(q))

print('Reflexão da componente x do 1° ponto: ', p.reflexao_x())
print('Reflexão da componente x do 2° ponto: ', q.reflexao_x())


################## INCLINAÇÃO EM RELAÇÃO A ORIGEM #################

#RETAS VERTICAIS
if p.x == 0 or q.x == 0:
    print('Seus pontos formam retas verticais')
else:
    print('Inclinação da reta que une a origem ao 1º ponto: ', p.inclinacao_da_origem())
    print('Inclinação da reta que une a origem ao 2º ponto: ', q.inclinacao_da_origem())

#RETAS HORIZONTAIS
if p.y == 0 or q.y == 0:
    print('Seus pontos formam retas horizontais')
else:
    print('Inclinação da reta que une a origem ao 1º ponto: ', p.inclinacao_da_origem())
    print('Inclinação da reta que une a origem ao 2º ponto: ', q.inclinacao_da_origem())
    
##########################################################################

################# PARÂMTROS DA RETA ########################
if p.x == q.x and p.y != q.y:
    print('Reta vertical')
elif p.x == q.x and p.y == q.y:
    print('Ponto em cima de outro pronto')
else:    
    print('Parêmtros a e b para equação da reta: ', p.parametros_reta(q))

#if p.x == q.x and p.y == q.y:
#    print('pont')
#else:
#    print('Parêmtros a e b para equação da reta: ', p.parametros_reta(q))
