def classifica_lista(l):
    crescente = 0
    decrescente = 0
    if len(l) < 2 :
        return 'nenhum'
    else:
        for i in range(len(l)):
            if l[i+1]>l[i]:
                crescente += 1
            elif  l[i+1]<l[i]:
                decrescente += 1
            else:
                pass
        if decrescente == len(l) :
            return 'decrescente'
        elif crescente == len(l) :
            return 'crescente'
        else:
            return 'nenhum'
                    
