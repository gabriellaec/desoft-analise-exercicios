def eh_primo(n):
    i=3
    while n>3 and i<n:
        if n%2==0:
            return False
        else:
            if n%i==0:
                return False
            else:
                return True
        i+=2
        
    if n == 0 or n == 1:
        return False
    if n ==2 or ==3:
        return True
            
        