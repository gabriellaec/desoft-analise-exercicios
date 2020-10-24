def eh_primo (x):
    y=3
    a=True
    while a:
        if x>y and x%y==0:
            y=y+2
            return False
        elif x==y:
            return False
    if x==1 and x==0:
        return False
    elif x==2:
        return True
    elif x>1:
        if x%2==0:
        return False
    
            
            
    