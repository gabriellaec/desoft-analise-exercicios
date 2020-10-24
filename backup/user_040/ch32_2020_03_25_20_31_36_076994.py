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
    if n!=0 and n < 2:
        lista[0]=2
    elif n!=0 and n>=2:
        lista[0]=2
        lista[1]=3
    
    a=2
    while a<n:
        if eh_primo(lista[a-1]+2)==True:
            lista[a]=lista[a-1]+2
            a+=1
        elif eh_primo(lista[a-1]+2)==False:
            lista[a]=lista[a-1]+4
            a+=1
        elif eh_primo(lista[a-1]+2)==False and eh_primo(lista[a-1]+4)==False:
            lista[a]=lista[a-1]+6
            a+=1
        elif eh_primo(lista[a-1]+2)==False and eh_primo(lista[a-1]+4)==False and eh_primo(lista[a-1]+6)==False:
            lista[a]=lista[a-1]+8
            a+=1
        
    
    return lista

        
