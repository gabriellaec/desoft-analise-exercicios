def eh_primo(n):
    
    i=1
    
    while i<n:
        if n%2==0:
            return False
        elif i%2==0:
            return False
        i+=2

    if n==0 or n==1:
        return False

    if n==2:
        return True
    
    else:
        return True