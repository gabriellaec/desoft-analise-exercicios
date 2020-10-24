def classifica_lista(lista):
    if lista==[]:
        return 'nenhum'
    for i in range(len(lista)-1):
        if lista[i+1]<=lista[i]:
            return 'decrescente'
        if lista[i+1]>=lista[i]:
            return 'crescente'
        if len(lista)>2:
            return 'nenhum'
        else:
            return 'nenhum'
    
    
