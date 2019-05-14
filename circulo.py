import math
from ponto import *

class Circulo:
    """ Caracteriza um círculo.
    atributos:
    - centro: tipo Ponto
    - raio: tipo float
    """

    def __init__(self, raio, centro = Ponto()):
        self.r = raio
        self.p = centro

    def ponto_no_circulo(self, alvo):
        """ Informa se um ponto está dentro do circulo """
        d = alvo.distancia_dois_pontos(self.p)
        return d <= self.r
