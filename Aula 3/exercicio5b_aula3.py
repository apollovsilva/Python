import math

def volume_esf(r):
    volume = (4/3)*math.pi*r**3
    return volume

r = float(input('Digite o raio da esfera em metros: '))

x = volume_esf(r)

print('Volume da esfera: ',x)
