comp_onda = 632.8*10**(-9)     #metros

dist_anteparo = 1.98           #metros

esp_fendas = 0.250*10**(-3)    #metros

delta_y = (comp_onda*dist_anteparo)/(esp_fendas)  #distância entre dois máximos de interferência consecutivos

print("{0:.5f}".format(delta_y))
