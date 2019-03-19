print('Se você fizer uma corrida de 10 quilômetros em 43 minutos e 30 segundos, qual será seu tempo médio por milha? Qual é a sua velocidade média em milhas por hora? (Dica: há 1,61 quilômetros em uma milha).')

print('Caculando o tempo médio por milha')

print('Conversão de Km para milha')

y = float(input('Digite o valor da distância percorrida (em Km): '))

x = y/1.61

print('Distância em milhas: ', x)

print('Conversão de min para hora')

min =float (input('Digite o valor em minutos: '))

t1 = min/60

print('Tempo em hora: ', t1)

print('Conversão de seg para hora')

seg = float (input('Digite o valor em segundos: '))

t2 = seg/3600

print(t2)

print('Tempo em horas', t2)

h = t1 + t2

print('Logo o tempo total será: ', h)

print('Agora o tempo por milha')

tempmil = h/x

print('Tempo por milha: ', tempmil)

print('Cáculo da velocidade em milhas por hora')

v = x/h

print('vel em milhas por hora: ', v)
