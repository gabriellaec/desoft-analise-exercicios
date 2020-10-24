def eh_primo(x):
    i= 3
    if(x==2):
        return True
    elif(x==1):
        return False
    elif(x==0):
        return False
    elif(x==3):
        return True    
    elif(x%2==0):
        return False    
    while(x > i):
        if(x%i==0):
            return False
        i= i + 2        
    return True
        
def lista_primos(z):
    primos=[]
    i=1    
    while len(primos)<z:
        if eh_primo(i)==True:
            primos.append(i)
        i+=1
    return primos