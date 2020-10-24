def eh_primo (x):
    if x==1 and x==0:
        return False
    elif x==2:
        return True
    elif x>1:
        if x%2==0:
        return False
        else:
            y=3
            a=True
            while a:
                if x>y and x%y==0:
                    return False
                elif x==y:
                    return True
                    a=False
                y=y+2
        
    
            
            
    