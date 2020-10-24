def classifica_lista(x):
    x=[]
    i=0
    for e in x:
        i+=1
        if x[i]<x[i+1]:
            return 'crescente'
        elif x[i]>x[i+1]:
            return 'decrescente'
        elif len(x)<2:
            return 'nenhum'
        else:
            return 'nenhum'