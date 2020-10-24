def estritamente_crescente(lista):
    lista_sequencia = [lista[0]]
    maior = lista[0]
    
    i = 0
    while i < len(lista):    
        if lista[i] > maior:
            maior = lista[i]
            lista_sequencia.append(lista[i])
        i += 1   
    return lista_sequencia