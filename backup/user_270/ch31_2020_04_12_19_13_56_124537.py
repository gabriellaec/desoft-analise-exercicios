def eh_primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        i = 0
        for i in range(2,n+1):
            if n % i == 0 :
                i += 1
        if i == 1:
            return True
        else:
            return False
                
                
                
           
        
                