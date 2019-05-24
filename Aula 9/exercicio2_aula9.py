import os

def walk(dirname):
    """Printa todos os arquivos de um dado diretorio assim como de seus subdiretorios.
    dirname: nome de string do  diretorio
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)     # vai mostrar o nome do arquivo (file)
        else:
            walk(path)      # se não for um arquivo, mostrará o diretório e os arquvos dentro do mesmo

if __name__ == '__main__':
    walk('.')
