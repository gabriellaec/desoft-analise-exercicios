def lista_primos(n):
    contador=0
    lista=[]
    primo=0
    i = 3
    if p<=1:
        p+=1
    if p%2==0:
        if p==2:
            lista.append(p)
            contador+=1
            p+=1
        else:
            p+=1
    else:
        while i<n:
            if n%i==0:
                p+=1
            else:
                i+=2
                lista.append(p)
                p+=1
    return lista