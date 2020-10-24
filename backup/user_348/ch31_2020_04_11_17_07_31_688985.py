def eh_primo (n):
    p = 3
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    while n>=p:
        if (n%2==0):
            return False 
        elif(n%p == 0):
            return False
        p = p + 2
    return True
            