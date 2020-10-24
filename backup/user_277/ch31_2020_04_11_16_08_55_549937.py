def eh_primo(n):
    i=2
    j=0
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    while i>=n:
        a=n/i
        i+=1
    if a==0:
        return True
    else:
        return False