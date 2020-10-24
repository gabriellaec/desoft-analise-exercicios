def primos_entre(a,b):
    j=a
    x=2
    lista=[]
    while x<=j and j<=b:
        resto = j % x
        if resto == 0 and x!=j:
            j+=1
        elif x==j:
            lista.append(j)
            j+=1
            x=2
        else:
            x+=1
    return len(lista)