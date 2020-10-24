def lista_primos(n):
    t=0
    n=2
    lista=[0]*n
    while n>t:
        div=2
        while n>=div:
            if n%div==0:
                break
            else:
                div+=1
        if n==div:
            lista[t]=n
            t+=1
        n+=1
    return lista