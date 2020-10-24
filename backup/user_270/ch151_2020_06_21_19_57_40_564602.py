def classifica_lista(l):
    crescente = 0
    decrescente = 0
    if len(l) < 2 :
        return 'nenhum'
    else:
        for i in range(len(l)):
            if l[i]>l[i-1]:
                decrescente += 1
            elif  l[i]<l[i-1]:
                crescente += 1
            else:
                pass
        if decrescente == len(l)-1 :
            return 'decrescente'
        elif crescente == len(l)-1 :
            return 'crescente'
        else:
            return 'nenhum'
                    
