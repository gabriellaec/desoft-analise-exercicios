def separa_trios(lista):
    x = 3
    l = []
    for i in range(len(lista), ,3):
        l += lista[ i: x:3]
        x+=3
    return l