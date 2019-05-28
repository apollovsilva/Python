from aula9pt2_ex3 import*
import numpy as np
import matplotlib.pyplot as plt

x, y, z = ler_arquivos('dados_alunos.txt')

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
