def lista_caracteres(n):
    a=list(n)
    nova=[]
    i=0
    while i<len(a):
        if a[i] not in nova:
            nova.append(a[i])
            i+=1
        else:
            i+=1
    return nova
        