def lista_primos(n):
    lista=[0]*n
    x=2
    if n!=0:
        lista[0]=2
    elif n!=0 and n>=2:
        lista[0]=2
        lista[1]=3
    
    while 1<x<n:
        y=3
        lista[x]%2!=0 and lista[x]%y!=0 and lista[x]>lista[x-1]
        x+=1
    
    return lista

        
