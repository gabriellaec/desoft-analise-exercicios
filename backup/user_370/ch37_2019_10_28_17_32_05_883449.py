def eh_primo(x):
    if x==0:
        return False 
    elif x==1:
        return False
    elif x==2:
        return True
    elif x % 2==0:
        return False
    else:
        y=x-2
        while y>2:
            if x%y==0:
                return False 
            y=y-2
        return True  
    
def lista_primos(x):
    lista=[]
    lista_ordem_crescente=[]
    i=0
    a = eh_primo(x)
    while i < x:
        if a == True:
            lista.append(i)
        elif lista[i] < lista[i+1]:
            lista_ordem_crescente.append(lista[i])
        else:
            lista.append(lista[i])
            
    i+=1        
    return (lista)
    

        
    
    
 