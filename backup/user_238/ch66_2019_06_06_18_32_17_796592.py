def capitaliza(p):
    i=1
    l=[]
    p0=p[0].upper()
    l.append(p0)

    while i <=len(p)-1:
        l.append(p[i])
        i+=1
    m="".join(l)
    return m