def separa_trios(lista):
    x = 3
    l = []
    for i in range(0,len(lista),3):
        l.append(lista[ i: x:1])
        x+=3
    return l