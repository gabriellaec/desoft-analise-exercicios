def numero_no_indice(a):
    c=[]
    for i in range(len(a)):
        if a[i]==a.index(a[i]):
            c.append (i)
    return c
