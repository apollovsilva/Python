import math

print('Encontre as raízes de uma função do 2° grau')

a = float(input('Digite o valor de a: '))

b = float(input('Digite o valor de b: '))

c = float(input('Digite o valor de c: '))

x_1 = ((-b + math.sqrt(b**2 - 4*a*c)))/(2*a)

x_2 = ((-b - (b**2 - 4*a*c)**0.5))/(2*a)
       
print('1ª raiz: ', "{0:.2f}".format(x_1))

print('2ª raiz: ', x_2)       