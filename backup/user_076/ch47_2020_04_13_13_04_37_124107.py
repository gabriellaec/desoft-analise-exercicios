def estritamente_crescente(lista_aleatória):
    i = 0
    lista_crescente = []
    if len(lista_aleatória)>0:
        lista_crescente.append(lista_aleatória[0])
        while i<len(lista_aleatória)-1:
            if lista_aleatória[i+1] > lista_aleatória[i]:
                lista_crescente.append(lista_aleatória[i+1])
            i+=1
    return lista_crescente