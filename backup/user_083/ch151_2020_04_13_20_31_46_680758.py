def classifica_lista(lista):
    i=0
    if len(lista)<2:
        return 'nenhum'
    while i < (len(lista)):
        if lista[i+1]>lista[i] and lista[i+2]>lista[i+1]:
            return 'crescente'
            i+=1
        if lista[i+2]<lista[i+1]<lista[i]:
            return 'decrescente'
            i+=1
        if lista[i+1]==lista[i] or lista[i+1]>lista[i+2]:
            return 'nenhum'
            i+=1