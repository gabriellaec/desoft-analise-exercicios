def soma_valores(a):
    a=[]
    i=0
    while i<10:
        b=float(input('Nota: '))
        a.append(b)
        i+=1
    c=sum(a)
    return c