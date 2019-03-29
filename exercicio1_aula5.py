def find_val_max(x,y,z):
    if( x >= y and x > z):
        return x

    if( y > x and y >= z):
        return y
    
    if( z >= x and z > y):
        return z


x = float(input('Digite o primeiro valor: '))
y = float(input('Digite o segundo valor: '))
z = float(input('Digite o terceiro valor: '))

maior_valor = find_val_max(x,y,z)

print('O maior valor é: ',maior_valor)
