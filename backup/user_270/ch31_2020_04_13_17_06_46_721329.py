def eh_primo(n):
    k = 0
    if n < 2 :
        return False
    else:
        for i in range(1,n):
            if n % i != 0:
            k += 1
    if k == (n-1) :
        return True
    else:
        return False
                
                
           
        
                