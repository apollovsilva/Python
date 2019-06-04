import math
math.exp(0)-math.exp(-10)

x=range(0,10)
y=[math.exp(-xi) for xi in x]  # isto se chama "list comprehension"
print(x)
print(y)

import matplotlib.pyplot as plt
plt.bar(x,y,color="red",align="edge",width=1)
x1=[i/1000 for i in range(0,10000)]
y1=[math.exp(-xi) for xi in x1]
#plt.plot(x1,y1)
#plt.plot(x,y)
#plt.show()

S1= 0
for xi in x1:
    S1 = S1+ math.exp(-xi) * 0.001
print("Soma 1000 caixinhas = ",S1)

