def separa_trios(lista):
    a = len(lista)
    c = 0
    new = []
    for i in range(2, a, 3):
        c = lista[:2]
        new.append(c)
        c+=1
    return new
        
        