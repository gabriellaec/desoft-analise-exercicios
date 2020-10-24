y=3
def eh_primo (x):
    if x%2==0:
        return False
    while y<x:
        if x%y==0:
            y=y+2
            return False
        else:
            return True
            
            
    