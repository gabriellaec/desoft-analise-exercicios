def eh_primo (x) :
    if x==0:
        return False 
    elif x==1:
        return False 
    elif x==2:
        return True
    elif x==3:
        return True
    while x>3:
        if x%2==0:
            return False 
        else:
            return True 
