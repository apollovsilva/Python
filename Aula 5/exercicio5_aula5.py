def par(list):
    for num in list:
        if num % 2 == 0: #verificando se o resto da divisão de num por 2 resulta em 0, ou seja, você está verificando se x é múltiplo de 2
            print(num)

list = [10, 15, 33, 254, 1, 0, 1002]

par(list)
