def classifica_lista(lista)
    if len(lista)<2:
        return 'nenhum'
    w = lista[1]-lista[0]
    if w>0:
        for i in range (len(lista)-1):
            if lista[i]-lista[i+1]<=0:
                return 'nenhum'
    if w<0:
        for i in range (len(lista)-1):
            if lista[i]-lista[i+1]>=0:
                return 'nenhum'
    if w==0:
        return 'nenhum'
    elif w>0:
        return 'crescente'
    elif w<0:
        return 'decrescente'