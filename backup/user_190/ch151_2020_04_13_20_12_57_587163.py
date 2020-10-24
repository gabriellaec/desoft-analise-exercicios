def classifica_lista(x):
    i=0
    if len(x)<2:
        return 'nenhum'
    else:
        for e in x:
            i+=1
            if x[i]<x[i+1]:
                return 'crescente'
            elif x[i]>x[i+1]:
                return 'decrescente'
            else:
                return 'none'