def eh_primo(n):
    i=2
    validacao= 0
    if n==0 or n==1:
        return False
    while i<n:
        if n%i==0:
            validacao=1
            return False
        i+=1
    
    if validacao==0:
        return True
        