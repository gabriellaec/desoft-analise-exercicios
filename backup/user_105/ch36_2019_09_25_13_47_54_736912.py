def eh_primo (x):
    if x==2:
        return True
    elif x==1 or x==0:
        return False
    elif x%2==0:
        return False
    else:
        if x == 3:
            return True
        else:
            n = 3
            while n < x:
                if x%n==0:
                    return False
                else: 
                    return True
                n=n+2