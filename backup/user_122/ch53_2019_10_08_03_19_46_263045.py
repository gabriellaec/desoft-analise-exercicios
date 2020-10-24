def inverte_lista(lista):
    
    lista_original = input("Qual a lista?")
    lista_invertida = []
    i = len(lista_original)
    
    while (i <= len(lista_original)) and (i > 0):
        lista_invertida.append(lista_original[i])
        i -= 1
    return lista_invertida