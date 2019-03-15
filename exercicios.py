print('Cacular tempo médio por milha')

print('Conversão km para milha')

y = float(input('valor de y: '))

x = y/1.61

print(x)

print('Conversão min para hora')

min =float (input('colocar valor em minuto: '))

t1 = min/60

print(t1)

print('Conversão seg para hora')

seg = float (input('colocar valor em segundos: '))

t2 = seg/3600

print(t2)

print('tempo em horas')

h = t1 + t2

print('h = ',h)

print('cálculo tempo por milha')

tempmil = h/x

print('tempmil = ', tempmil)

print('cáculo da velocidade em milhas por hora')

v = x/h

print('v = ', v)
