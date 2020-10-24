def numero_no_indice(lista_n):
    listan = []
    i = 0
    while i < len(lista_n):
        if lista_n[i] == lista_n.index(lista_n[i]):
        	listan.append(lista_n[i])
        i += 1
        
    return listan
        