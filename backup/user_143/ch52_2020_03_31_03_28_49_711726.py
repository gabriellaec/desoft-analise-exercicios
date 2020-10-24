def calcula_total_da_nota(p, q):
    i=0
    c=0
    lista=[]
    s=0
    while i<len(p):
        a=p[i]
        b=q[i]
        c=a*b
        lista.append(c)
        i+=1
        d=0
        while d<len(lista):
            s+=lista[d]
            d+=1
    return s