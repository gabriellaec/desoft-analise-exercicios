def lista_primos(n):
    lista=[0]*n
    x=2
    y=3
    if n!=0:
        lista[0]=2
    elif n!=0 and n>=2:
        lista[0]=2
        lista[1]=3
    
    while x<n:
        if lista[x]%2!=0 and lista[x]%y!=0:
            lista[x]=lista[x-1]+2
        elif lista[x]%2!=0 and lista[x]%y!=0 and lista[x]!=lista[x-1]+2:
            lista[x]=lista[x-1]+4
        y+=2
        x+=1
        
    
    return lista

        
