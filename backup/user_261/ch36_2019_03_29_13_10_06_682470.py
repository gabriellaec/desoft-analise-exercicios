def eh_primo(n):
    i=1
    r=n%2
    if r==0:
        return False
    while i<n:
        a=n%i
        if a==0:
            return False
        else:
            i+=2
    return True

