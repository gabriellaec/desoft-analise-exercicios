def eh_primo(n):
    i=2
    r=n%2
    if r!=2 and r==0:
        return False
    while i<n:
        a=n%i
        if a==0:
            return False
        else:
            i+=1
    return True

