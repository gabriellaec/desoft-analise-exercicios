def classifica_lista(l1):
    
    for i in range(len(l1)-1):
        if l1[i+1]<=l1[i]:
            return 'decrescente'
        if l1[i+1]>=l1[i]:
            return 'crescente'
        if len(l1)<2:
            return 'nenhum'
        else:
            return 'nenhum'