def estritamente_crescente(lista):
    lista_sequencia = []
    maior = lista[0]
    lista_sequencia.append(lista[0])
    i = 0
    while i < len(lista):    
        if lista[i] > maior:
            maior = lista[i]
            lista_sequencia.append(lista[i])
        i += 1   
    return lista_sequencia