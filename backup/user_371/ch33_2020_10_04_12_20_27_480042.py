def lista_primos(a,b):
    j=a
    x=2
    numero_de_primos=0
    lista=[]
    while x<=j and j<=b:
        resto = j % x
        if resto == 0 and x!=j:
            j+=1
        elif x==j:
            lista.append(j)
            numero_de_primos+=1
            j+=1
            x=2
        else:
            x+=1
    return numero_de_primos