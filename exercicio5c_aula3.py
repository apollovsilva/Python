# distância entre 2 máximos de interferência consecutivos

def dist_max(comp_onda,dist_anteparo,esp_fendas):
    dist_maxima = (comp_onda*dist_anteparo)/(esp_fendas)
    return dist_maxima

def nm_metros(comp_onda):
    metros = comp_onda*10**(-9)
    return metros

def mm_metros(esp_fendas):
    metros = esp_fendas*10**(-3)
    return metros

# todos os dados estão em metros

comp_onda = nm_metros(float(input('Digite o comprimento de onda em nm: ')))
dist_anteparo = float(input('Digite o valor da distância do anteparo (D) em metros: '))
esp_fendas = mm_metros(float(input('Digite o valor do espaçamento entre as fendas em metros: ')))
              
x = dist_max(comp_onda,dist_anteparo,esp_fendas)

print('Distância entre dois máximos: ',x)
