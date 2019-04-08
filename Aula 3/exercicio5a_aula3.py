def imc(massa,altura):
    imc = massa/altura**2
    return imc

# imc de uma pessoa qualquer

massa = float(input('Digite sua massa em Kg: '))
altura = float(input('Digite sua altura em metros: '))

y = imc(massa,altura)

print('Seu imc: ',y)

# imc de um bebê

x = imc(11,0.7)

print('IMC de um bebê de 70cm e 11g: ', x)
