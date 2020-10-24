def eh_primo(x):
    i= 3
    if(x==2):
        return True
    elif(x==1):
        return False
    elif(x==0):
        return False
    
    
    elif(x%2==0):
        return False
    
    while(x > i):
        if(x%i==0):
            return False
        else:
            return True
        
        i= i + 2