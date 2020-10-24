def eh_primo (x) :
    i=3
    if x%2==0:
        return True
    elif x%1==0:
        return False
    elif x==0:
        return False
    else: 
        while i<=x:
            i+=2
            x%i!=0
            return True
            
    
