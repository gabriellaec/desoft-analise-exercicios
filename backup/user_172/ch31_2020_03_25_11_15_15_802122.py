 y=3
def eh_primo (x):
    while y<x:
        if x%y==0:
            y=y+2
            return False
        else:
            return True
    if x!=2 and x!=1 and x%2==0:
        return False
    elif x==1:
        return False
    elif x==2:
        return True
            
            
    