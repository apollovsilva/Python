import math

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
        return Ponto(self.x, -self.y)

    def inclinacao_da_origem(self):
        m = self.y/self.x
        return m

    def parametros_reta(self, alvo):
        a = (self.y - alvo.y)/(self.x - alvo.x)
        b = (self.y * alvo.x - self.x * alvo.y)/(alvo.x - self.x)
        return Ponto(a, b)
