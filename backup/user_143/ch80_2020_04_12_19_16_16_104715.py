def interseccao_chaves (d1, d2):
    l=[]
    for i in d1.keys(): 
        c=i
        for j in d2.keys():
            d=j
            if c==d:
                l.append(c)
                j=len(d2)
    return l