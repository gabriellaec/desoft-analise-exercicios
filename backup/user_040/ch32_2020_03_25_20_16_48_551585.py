def eh_primo(x):
    y = 3
    if (x%2==0 and x!=2 or x==1 or x==0):
        return False
    
    while x>y:
        if x%y==0:
            return False
        y+=2
    return True

def lista_primos(n):
    lista=[0]*n
    x=2
    y=3
    if n!=0 and n < 2:
        lista[0]=2
    elif n!=0 and n>=2:
        lista[0]=2
        lista[1]=3
    
    while eh_primo==True:
        if lista[x]%2!=0 and lista[x]%y!=0:
            lista[x]=lista[x-1]+2
        elif lista[x]%2!=0 and lista[x]%y!=0 and lista[x]!=lista[x-1]+2:
            lista[x]=lista[x-1]+4
        y+=2
        x+=1
        
    
    return lista

        
