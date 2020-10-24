def verifica_lista(l):
    p = False
    i = False
    for i in l:
        if i % 2 == 0:
            p = True
        else:
            i = True
    if p and i == True:
        return("misturado")
    elif p == True and i == False:
        return("par")
    elif len(l) == 0:
        return("misturado")
    elif p == False and i == True:
        return("ímpar")