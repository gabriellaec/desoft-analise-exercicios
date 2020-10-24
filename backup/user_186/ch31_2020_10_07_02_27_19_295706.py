def eh_primo (x) :
    i=3
    if x==2:
        return True
    if x!=2 and  x%2==0:
        return False
    elif x%1==0:
        return False
    elif x==0:
        return False
    else: 
        while i<x:
            i+=2
            if x%i==0:
                return False
            else:
                return False
            
    
