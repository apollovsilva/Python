def vel_media(si, sf, t):
    v_m = (sf - si)/t
    print(v_m)
    
print('CALCULAR VELOCIDADE MÉDIA - MRU')

si = float(input('Digite a posição inicial em metros: '))
sf = float(input('Digite a posição final em metros: '))
t = float(input('Digite o tempo em segundos: '))

vel_media(si, sf, t)

def vel_mrua(a, t):
    v_mrua = a*t
    print(v_mrua)
    
print(' ')
print('VELOCIDADE FINAL DE UM OBJETO EM QUEDA LIVRE - MRUV')

a = float(input('Digite o valor da aceleração em m/s²: '))
t = float(input('Digite o tempo de queda em segundos: '))

vel_mrua(a, t)
