def dobrar_elementos(uma_lista):
    """ Reescreve os elementos de uma_lista com o dobro de seus valores originais.
    """
    lista_original = uma_lista[:]
    
    for (i, valor) in enumerate(uma_lista):
        novo_elem = 2 * valor
        lista_original[i] = novo_elem
        
    return lista_original



minha_lista = [2, 4, 6]
print(minha_lista)
print(dobrar_elementos(minha_lista))
