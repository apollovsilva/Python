import os

def walk(dirname):
    """Printa todos os arquivos de um dado diretorio assim como de seus subdiretorios.
    dirname: nome de string do  diretorio
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

if __name__ == '__main__':
    walk('.')
