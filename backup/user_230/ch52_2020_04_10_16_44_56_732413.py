def calcula_total_da_nota(a, b):
    c=[]
    if a==[] and b==[]:
        return a
    for i in range(len(a)):
        for i in range(len(b)):
            c[i]=a[i]*b[i]
    sum(c)
    return c
        
        