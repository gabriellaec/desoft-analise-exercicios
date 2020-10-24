def eh_primo(n):
    
    i=3
    if n==2:
        return True

    while i<n:
        if n%2==0:
            return False
        elif n%i==0:
            return False
        i+=2

    if n==0 or n==1:
        return False

   
    
    else:
        return True