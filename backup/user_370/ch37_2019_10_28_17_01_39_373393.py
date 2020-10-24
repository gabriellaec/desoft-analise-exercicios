def eh_primo(x):
    if x==0:
        return False 
    elif x==1:
        return False
    elif x==2:
        return True
    elif x%2==0:
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
    i=0
    a = eh_primo(x)
    while i < x:
        if a == True:
            lista.append(i)
            i+=1
    return (lista)
    

        
    
    
 