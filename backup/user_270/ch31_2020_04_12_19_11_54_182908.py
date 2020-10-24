def eh_primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        i = 0
        for i in range(2,n):
            if n % i == 0 :
                i += 1
        if i == 0:
            return True
        else:
            return False
                
                
                
           
        
                