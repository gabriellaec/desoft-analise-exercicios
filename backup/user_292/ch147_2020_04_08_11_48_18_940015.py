def mais_frequente(lista):
    dm = {}
    for i in lista:
        if i not in dm:
            dm[i] = 1 
        else: 
            dm[i] +=1
    C = 0
    P = ''
    for p,c in dm.items():
        if c > C:
            C = c
            P = p
    return P