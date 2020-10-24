def calcula_fibonacci(n):
    a=1
    b=1
    i=2
    c=0
    lista=[]
    if n==1:
        lista.append(a)
    elif n>1:
        lista.append(a)
        lista.append(b)
        while i<n:
            c=a+b
            lista.append(c)
            a=b
            b=c
            i+=1
    return lista