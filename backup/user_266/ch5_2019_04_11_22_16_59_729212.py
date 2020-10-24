def maior_primo_menor_que(n):
    lista=[]
    c=True
    for i in range(1,n+1):
        if n%i==0:
            lista.append(1)
        if len(lista)>2 or n==1 or n<=0:
            c=False
            return c
            break
    return c