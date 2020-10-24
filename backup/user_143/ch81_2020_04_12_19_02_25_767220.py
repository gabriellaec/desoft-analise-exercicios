def interseccao_valores (d1, d2):
    li=[]
    for i in range(len(d1)):
        a=0
        c=d1[i].values()
        while a<len(d2):
            d=d2[a].values()
            if c==d:
                li.append(c)
                a=len(d2)
            else:
                a+=1
    return li