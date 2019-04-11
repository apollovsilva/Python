#multiplica cada valor da lista

def mult(list):
    x = list[0]
    for i in range(1,len(list)):
        x = x*list[i]
        print(x)

list = [1,2,3]

mult(list)
#print(soma(list))

