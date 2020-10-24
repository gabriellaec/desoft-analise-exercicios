def eh_primo (x):
    if x==2:
        return True
    elif x==0 or x==1:
        return False
    else:
        n = 3
        while n < x:
            if x%n==0:
                return False
            n += 2
        return True