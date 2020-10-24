def verifica_lista(l):
    p = False
    i = False
    for i in l:
        if i % 2 == 0:
            p = True
        if i % 2 != 0:
            i = True
    if len(l) == 0:
        return "misturado"
    if p == True and i == True:
        return "misturado"
    if p == True and i == False:
        return "par"
    if p == False and i == True:
        return "ímpar"
