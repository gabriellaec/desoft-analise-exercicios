def interseccao_chaves (d1, d2):
    l=[]
    for i in d1.keys(): 
        l.append(i)
    for j in d2.keys():
        l.append(j)
    return l