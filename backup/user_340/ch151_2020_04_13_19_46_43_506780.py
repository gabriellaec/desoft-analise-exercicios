def classifica_lista(lista):
    if len(lista)==1 and lista==[]:
    return 'nenhum'
    for t in range(len(lista)-1):
        if lista[t+1]<=lista[t]:
        return 'decrescente'
        else:
        return 'crescente'
            
    