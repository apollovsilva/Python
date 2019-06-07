import math
import matplotlib.pyplot as plt
math.exp(0)-math.exp(-10)

x=range(0,10)
y=[math.exp(-xi) for xi in x]  # isto se chama "list comprehension"
print(x)
print(y)

plt.bar(x,y,color="red",align="edge",width=1)
x1=[i/100 for i in range(0,1000)]
y1=[math.exp(-xi) for xi in x1]
plt.plot(x1,y1)
#plt.show()

S1 = 0
xfim = 10
I_a = 1 - math.exp(-xfim)
n = 100

while abs(S1- I_a)/I_a > 0.01 :
    S1 =0
    dx = xfim/n
    xi=0
    for i in range (0,n):
        S1 += math.exp(-xi) * dx
        xi += dx
    n += 1
    print(S1)
    
print("Soma {0} caixinhas = {1}".format(n-1,S1))
