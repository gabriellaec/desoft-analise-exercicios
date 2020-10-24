def classifica_lista(x):
    a = 1
    while a<len(x):
        if x[a-1] < x[a]:
            a+=1
            return 'crescente'
        elif len(x) < 2:
            return 'nenhum'
        elif x[a-1] > x[a]:
            return 'decrescente'
        elif x == []:
            return 'nenhum'
        else:
            return 'nenhum'
            
            