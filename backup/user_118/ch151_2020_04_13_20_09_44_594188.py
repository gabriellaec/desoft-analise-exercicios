def classifica_lista(lista):
    i=0
    while i<len(lista)>=2:
        if lista[i]>lista[i+1]:
            return 'decrescente' 
        elif lista[i+1]>lista[i]:
            return 'crescente'
        else:
            return 'nenhum'
    while len(lista)<2:
        return 'nenhum'
