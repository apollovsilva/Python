class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancia_de_origem(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def ponto_medio(self, alvo):
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto(mx, my)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def reflexao_x(self):
        return Ponto(- self.x, self.y)

p = Ponto()
q = Ponto()

p.x = float(input('Digite a coordenada x do ponto inicial: '))
p.y = float(input('Digite a coordenada y do ponto inicial: '))
q.x = float(input('Digite a coordenada x do ponto final: '))
q.y = float(input('Digite a coordenada y do ponto final: '))

print('Ponto médio: ', p.ponto_medio(q))

print('refelxão: ', p.reflexao_x())
