def milhas_m(milha): # milha para metros
    x = 1610*milha
    return x

def m_milhas(metros): # metros para milha
    x = metros/1610
    return x

def horas_seg(horas): # hora para segundo
    x = 3600*horas
    return x

def seg_horas(seg): # segundo para hora
    x = seg/3600
    return x

def min_horas(minu): # minuto para hora
    x = minu/60
    return x

def temp_milhas(z,d):
    temp_milha = (1.61*z)/d
    return temp_milha

x = min_horas(43)
y = seg_horas(30)
z = x + y

print(x, ' minuto em horas')
print(y, ' segundos em horas')
print(z, ' tempo total em horas')

# tempo (em horas) por milha

print(temp_milhas(z,float(input('distância percorrida em metros: '))) , ' tempo por milha')

# velociade média em milhas por hora

v = m_milhas(10000)/z

print(v, 'velocidade em milhas por horas')
