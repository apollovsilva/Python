d0 = 0
dfin = 5
v = 12

t = [i for i in range(0,30)] # intervalo de 0 a 30 pq quis, poderia ser outro valor
                             # mas tem q ser um intervalo tal que dfim esteja
                             # para obter então o tempo total em 5km

d = [d0 + (v/60)*ti for ti in t] # velocidade em km/min

print(d)              # print da lista de posição

i=d.index(5)          # pega o item da lista que tem valor igual a 5
                      # e calcula o tempo para tal distancia (item da lista)
                      
print("O atleta percorreu {0} kilômetros em {1} minutos".format(d[i],t[i]))
