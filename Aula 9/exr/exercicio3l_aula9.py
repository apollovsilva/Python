def primeiro_div21(n):
    for x in range(101,n):
        if (x % 21 != 0):
            print(x, 'não e div por 21')
        else:
            print(x, 'é div por 21')
            return

n = int(input('Digite um valor maior q 101: '))

primeiro_div21(n)
