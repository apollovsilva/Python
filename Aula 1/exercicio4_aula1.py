# ângulo zenital do sol

import math

sombra = 0.5

altura = 5

theta = math.atan(sombra/altura)

print("{0:.2f}".format(theta))

print("{0:.2f}".format(math.degrees(theta)))
