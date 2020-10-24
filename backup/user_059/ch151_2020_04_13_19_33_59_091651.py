def classifica_lista(lista):
    if len(lista)<1:
        return 'nenhum'
    else:
        cre = True
        for i in range(len(lista)-1):
            if lista[i+1] > lista[i]:
                pass
            else:
                cre = False
        dec = False
        for e in range(len(lista)-1):
            if lista[e+1] < lista[e]:
                dec = True
            else:
                pass
        if cre == True:
            return 'crescente'
        elif dec == False:
            return 'decrescente' 
        elif dec == False and cre == True:
            return 'nenhum'