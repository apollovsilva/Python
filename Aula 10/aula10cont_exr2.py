d0 = 0
d01 = 5
d02 = 5.2
dfin = 7

v1 = 12
v2 = 15
a = 202.5

t1 = [i for i in range(0,30)]        # intervalo de 0 a 30 pq quis, poderia ser outro valor
                                     # mas tem q ser um intervalo tal que dfim esteja
                                     # para obter então o tempo total em 5km
t2 = [i for i in range(30,60)]
t3 = [i for i in range(60,100)]


d1 = [d0 + (v1/60)*ti for ti in t1]                        # velocidade em km/min
d2 = [d01 + (v1/60)*ti + (a/2)*ti**2 for ti in t2]
d3 = [d02 + (v2/60)*ti for ti in t3]





print(d)              # print da lista de posição

i=d.index(5)          # pega o item da lista que tem valor igual a 5
                      # e calcula o tempo para tal distancia (item da lista)
                      
print("O atleta percorreu {0} kilômetros em {1} minutos".format(d[i],t[i]))
