from aula9pt2_ex3 import*
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import tstd

def sonic(x):
    print("Desvio padrao populacional:  ", np.std(x))
    print("Desvio padrao amostral: ", tstd(x))
    print("Media: ", np.mean(x))
    return np.std(x), tstd(x), np.mean(x)

x, y, z = ler_arquivos('dados_alunos.txt')

print("Figura 1: ")
sonic(x)
print("Figura 2: ")
sonic(y)
print("Figura 3: ")
sonic(z)

bins_x = np.linspace(15, 45, 30)
bins_y = np.linspace(1.5, 2, 30)
bins_z = np.linspace(40, 120, 30)

plt.figure(1)
plt.hist(x, bins_x, histtype='bar', rwidth=0.8)
plt.title('Primeira Coluna')
plt.figure(2)
plt.hist(y, bins_y, histtype='bar', rwidth=0.8)
plt.title('Segunda Coluna')
plt.figure(3)
plt.hist(z, bins_z, histtype='bar', rwidth=0.8)
plt.title('Terceira Coluna')
plt.show()
