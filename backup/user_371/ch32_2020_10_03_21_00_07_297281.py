def lista_primos(n):
    j=2
    x=2
    lista=[]
    while x<=j and len(lista)<n:
        resto = j % x
        if resto == 0 and x!=j:
            j+=1
        elif x==j:
            lista.append(j)
            return(j)
            j+=1
            x=2
        else:
            x+=1