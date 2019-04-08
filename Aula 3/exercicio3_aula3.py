# ângulo zenital do sol

import math
def angulo_zenital(sombra, altura):
    theta = math.atan(sombra/altura)
    print("{0:.4f}".format(theta)) #radianos
    print("{0:.2f}".format(math.degrees(theta))) #graus
    
sombra = float(input('Digite o tamanho da sobra projetada em metros: '))
altura = float(input('Digite o valor da altura em metros: '))

angulo_zenital(sombra, altura)