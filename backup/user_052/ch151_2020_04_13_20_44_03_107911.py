def classifica_lista(L):
    if len(L) < 2:
        print ("nenhum")
    else:
        crescente = True
        decrescente = True
        for i in range(len(L)-1):
            if L[i+1] < L[i]:
                crescente = False
            elif L[i+1] > L[i]:
                decrescente = False
        if crescente:
            return ("crescente")
        elif decrescente:
            return ("decrescente")
        else:
            return ("nenhum")
