def eh_primo (x):
    if x%2==0:
        return False
    elif x==1:
        return False
    elif x==2:
        return True
    y=3
    while y<x:
        if x%y==0:
            y=y+2
            return False
        else:
            return True
            
            
    