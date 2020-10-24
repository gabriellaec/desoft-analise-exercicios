def eh_primo(x):
    y=2

    if x==2:
        return True    
    if x==0 or x==1:
        return False
    while x>y:        
        if x%y==0:
            return False        
        y+=1
    return True