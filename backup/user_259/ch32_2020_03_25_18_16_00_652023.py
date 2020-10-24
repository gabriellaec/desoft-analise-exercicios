def lista_primos(n):
    lista=[]
    c=0
    while c<n:
        i = 3
        if c<=1:
            c+=1
        if c%2==0:
            if c==2:
                lista.append(c)
                c+=1
            else:
                c+=1
        else:
            while i<c:
                if c%i==0:
                    c+=1
                    i+=2
                else:
                    i+=2
            lista.append(c)
    return lista
    
