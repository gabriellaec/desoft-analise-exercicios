def separa_trios(lista):
    a = len(lista)
    c = 0
    new = []

    for i in range(2, a, 3):
        if lista[i:] < 3:
            new.append(lista[i:])
        c = lista[:i]
        new.append(c)
        c+=1
    return new        
        
        