import matplotlib.pyplot as plt

d0 = 0       # distancia inicial
d01 = 5      # distancia onde começa a acelerar
d02 = 5.2    # distancia onde termina de acelerar 
dfin = 7     # distancia final

v1 = 12      # velocidade inicial (para começar a celerar)
v2 = 15      # velocidade obtida ao fim da aceleração
a = 202.5    # aceleração

t1 = [i for i in range(0,26)]        # tempo em minutos para o primeiro trecho
t2 = [i for i in range(25,26)]       # tempo em minutos para o segundo trecho
t3 = [i for i in range(26,55)]      # tempo em minutos para o trecho final


d1 = [d0 + (v1/60)*ti for ti in t1]                       
d2 = [-12 + (v1/60)*ti + (a/7200)*ti**2 for ti in t2]        
d3 = [70 + (v2/60)*ti for ti in t3]

t = t1 + t2 + t3
d = d1 + d2 + d3

print(d1)
print(d2)
print(d3)


#print(d)              # print da lista de posição

#i=d.index(5)          # pega o item da lista que tem valor igual a 5
                      # e calcula o tempo para tal distancia (item da lista)
                      
#print("O atleta percorreu {0} kilômetros em {1} minutos".format(d[i],t[i]))
plt.plot(t,d)
plt.xlabel("tempo(min)")
plt.ylabel("distancia(km)")
plt.show()
