def interseccao_valores (d1, d2):
    li=[]
    for i in d1.values():
        a=0
        c=i
        while a<len(d2):
            d=d2[a]
            if c==d:
                li.append(c)
                a=len(d2)
            else:
                a+=1
    return li