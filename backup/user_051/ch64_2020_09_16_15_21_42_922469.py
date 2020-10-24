def acha_bigramas(b):
    i=0
    lista=[]
    while i<len(b)-1:
        c=b[i]+b[i+1]
        if c not in lista:
            lista.append(c)
        i+=1
    return lista
b='babador'
q=acha_bigramas(b)
print(q)