def eh_primo (n):
    if n== 0 or n==1:
        return False
    elif n ==2:
        return True
    for i in range (3, n,2):
        if (n%i ==0):
            return False
    else:
        return True