def dobrar_elementos(uma_lista):
    """ Clona a lista usada como parâmetro e reescreve os elementos deste clone com o dobro de seus valores originais.
    """
    lista_clone = uma_lista[:]
    
    for (i, valor) in enumerate(uma_lista):
        novo_elem = 2 * valor
        lista_clone[i] = novo_elem
        
    return lista_clone



minha_lista = [2, 4, 6]
print(minha_lista)
print(dobrar_elementos(minha_lista))
