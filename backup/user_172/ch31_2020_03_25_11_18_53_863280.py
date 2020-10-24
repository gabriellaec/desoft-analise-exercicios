def eh_primo (x):
    y=3
    while y<x:
        if x%y==0:
            y=y+2
            return False
    if x!=2 and x!=1 and x%2==0:
        return False
    elif x==1:
        return False
    elif x==2:
        return True
    else:
        return True
            
            
    