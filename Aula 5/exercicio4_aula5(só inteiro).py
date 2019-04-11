def test_range(n):
    if n in range(99):
        print('está no intervalo: ', n)
    else :
        print("O número está fora do intervalo")

n = float(input('Adicione o número a ser testado: '))

test_range(n)