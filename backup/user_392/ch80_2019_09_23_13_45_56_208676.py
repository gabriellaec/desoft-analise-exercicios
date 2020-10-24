def interseccao_chaves(x,y):
    lis=[]
    for e1,e2 in zip(x,y):
        if e1 == e2:
           lis.append(e1)
    return lis
        