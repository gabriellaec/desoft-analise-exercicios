def quantos_uns(n):
    lista=list(n) 
    x=0
    for i in lista:
        if lista[i]==1:
            x=x+1

    return x