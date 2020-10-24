def eh_primo(x):
    y=x-2
    if x==0:
        return False 
    elif x==1:
        return False
    elif x==2:
        return True
    elif x%2==0:
        return False
    else:
        while y>2:
            if x%y==0:
                return False 
            y=y-2
        return True    
            
    
    
        
        
 