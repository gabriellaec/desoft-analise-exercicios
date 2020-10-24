def eh_primo(x):
    y = 3
    if (x%2==0 and x!=2 or x==1 or x==0):
        return ("False")
    
    while x>y:
        if x%y==0:
            return False
        y+=2
        
    return ("True")