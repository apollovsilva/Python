import numpy as np

def ler_arquivos(filename):
    try:
        fin = open(filename)
    except: 
        print('Nao me dirige a palavra, faz favor')
        return 

    x, y, z = np.loadtxt(filename, unpack='True')
    print("Primeira coluna: ", x)
    print("Segunda coluna: ", y)
    print("Terceira coluna: ", z)

def numero_colunas(filename):
    n_column = np.loadtxt(filename, dtype='str').shape[1]
    print("Numero de colunas: ", n_column)

ler_arquivos('dados_alunos.txt')
numero_colunas('dados_alunos.txt')
