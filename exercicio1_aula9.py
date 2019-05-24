import numpy as np
import matplotlib.pyplot as plt

a, b, c = np.loadtxt('dados_alunos.txt', unpack='True')

bins_a = np.linspace(15, 45, 30)
bins_b = np.linspace(1.5, 2, 30)
bins_c = np.linspace(40, 120, 30)

print(a)
print(b)
print(c)

plt.figure(1)
plt.hist(a, bins_a, histtype='bar', rwidth=0.8)
plt.title('Primeira Coluna')

plt.figure(2)
plt.hist(b, bins_b, histtype='bar', rwidth=0.8)
plt.title('Segunda Coluna')

plt.figure(3)
plt.hist(c, bins_c, histtype='bar', rwidth=0.8)
plt.title('Terceira Coluna')

plt.show()
