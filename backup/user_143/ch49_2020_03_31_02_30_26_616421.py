def inverte_lista (l):
    b=len(l)+1
    l1=[0]*b
    while b>0:
        y=l[b]
        l1.append(y)
        b-=1
    return l1
        
    