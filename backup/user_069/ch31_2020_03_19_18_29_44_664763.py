def eh_primo (n):
    div=3
    if n%2==0 and n!=2 or n==1 or n==0:
        return False
    
    while n>div:
        if n%div==0:
            return False
        div+=2
    return True