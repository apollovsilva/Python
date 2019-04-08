#velocidade final (queda livre)

import math

h = 3

g = 9.8

vf = math.sqrt(2*g*h)

print('velocidade final: ',"{0:.2f}".format(vf))

t = vf/g

print('tempo de queda: ',"{0:.2f}".format(t))
