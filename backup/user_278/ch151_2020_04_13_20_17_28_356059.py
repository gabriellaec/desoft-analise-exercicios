def classifica_lista(lista):
    
    if len(lista)==1 or lista==[]:
            return 'nenhum'
    for i in range(len(lista)-1):
        if lista[i+1]<=lista[i]:
            return 'decrescente'
        if lista[i+1]>=lista[i]:
            return 'crescente'
        else:
            return 'nenhum'