def separa_trios(lista):
    a = len(lista)
    c = 0
    new = []
    if a%3 == 0:
        for i in range(2, a, 3):
            c = lista[:i]
            new.append(c)
            c+=1
    return new        
        
        