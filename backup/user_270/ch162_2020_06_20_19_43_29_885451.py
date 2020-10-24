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
    elif p == True:
        return("par")
    else:
        return("ímpar")