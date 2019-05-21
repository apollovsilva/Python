import matplotlib.pyplot as plt

fin = open('dados_alunos.txt')
linhas = fin.readlines()

for line in linhas:
    column = line.strip().split()
    print(column)
    x = column
    x = list(map(float, column))
    plt.hist(x, bins=100, range=(0,60))
    plt.xlabel('oi')
    plt.ylabel('ola')
    plt.title('nao sei')
    plt.show()
