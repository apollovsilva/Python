from ponto import Ponto

class Retangulo:
    """Representa um retangulo. 

    atributos: 
    - largura, do tipo float
    - altura, do tipo float 
    - canto, do tipo Ponto.
    """
    def __init__(self, largura, altura, canto = Ponto()):
        """ l -> largura; h -> altura; canto um ponto """
        self.l = largura
        self.h = altura
        self.p = canto

    def area(self):
        """ Cálculo da área do retângulo """
        a = self.l * self.h
        return a

    def perimetro(self):
        """ Cálculo do perímetro do retângulo """
        p = 2 * self.l + 2 * self.h
        return p

    def ponto_canto(self):
        """ Printa o ponto do canto inferior esquerdo do retângulo"""
        print(self.p)

p = Ponto(6,12)

r = Retangulo(18,30,p)
print("Área de um retângulo de lado 18cm e altura 30cm: ", r.area())
print("Perímetro deste mesmo restângulo: ", r.perimetro())

r.ponto_canto()


