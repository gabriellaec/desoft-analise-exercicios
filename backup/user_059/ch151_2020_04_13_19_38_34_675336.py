def classifica_lista(lista):
    if len(lista)<=1:
        return 'nenhum'
    else:
        cre = True
        for i in range(len(lista)-1):
            if lista[i+1] > lista[i]:
                pass
            else:
                cre = False
        dec = True
        for e in range(len(lista)-1):
            if lista[e] > lista[e+1]:
                pass
            else:
                dec = False
        if cre == True:
            return 'crescente'
        elif dec == True:
            return 'decrescente' 
        else:
            return 'nenhum'