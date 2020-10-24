def calcula_fibonacci(n):
    a=1
    b=1
    i=0
    c=0
    lista=[]
    if n>0:
        lista.append(a)
        while i<n:
            c=a+b
            lista.append(c)
            a=b
            b=c
            i+=1
    return lista