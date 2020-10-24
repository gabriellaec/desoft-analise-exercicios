def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    for i in range(3,n,2):
        if n%2!=0:
            return True
        elif n%i!=0:
            return True
    return False