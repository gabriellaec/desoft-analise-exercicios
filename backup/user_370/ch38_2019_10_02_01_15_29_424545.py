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

def primos_entre (a,b):
    i=a+1
    contador=0 
    while i>a and i<b: 
        if eh_primo(i)==True:
            contador+=1
        i+=1
    return contador
    

    
    