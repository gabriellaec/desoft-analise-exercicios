def classifica_lista(lista):
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
            print ("crescente")
        elif decrescente:
            print ("decrescente")
        else:
            print ("nenhum")
        