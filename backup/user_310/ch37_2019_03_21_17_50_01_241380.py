def imprime_primos(a):
    lista_primos=[]
    
    n=2
    i=2
    while n<=a:
        if n%i==0:
            n+=1
            i+=1
        else:
            lista_primos.append(n)
            n+=1
            i+=1
    return lista_primos