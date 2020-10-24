def lista_primos(n):
    lista=[0]*n
    x=2
    if n!=0:
        lista[0]=2
    elif n!=0 and n>=2:
        lista[0]=2
        lista[1]=3
    
    while y<x<n:
        y=3
        lista[x]%2!=0 and lista[x]%y!=0
        x+=1
        y+=2
    
    return lista

        
