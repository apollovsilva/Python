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
    return x, y ,z

def numero_colunas(filename):
    n_column = np.loadtxt(filename, dtype='str').shape[1]
    return n_column

if __name__ == '__main__':
    ler_arquivos('dados_alunos.txt')
    ler_arquivos('dados_alunos1.txt')
    print("Numero de colunas: ", numero_colunas('dados_alunos.txt'))
