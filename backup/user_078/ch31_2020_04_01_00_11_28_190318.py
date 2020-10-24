def eh_primo (u):
    i=3
    if u==2 or u==3:
        return True
    elif u%2==0 or u==1 or u==0:
        return False
    else:
        while u%i !=0 and u>i:
            i+=2
        if u==i:
            return True 
        else:
            return False