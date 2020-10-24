def eh_primo(n):
    i = 3
    while n>3 and i<n:
        while n %2 !=0:
            if n%i !=0:
                return True
            else:
                return False
        i+=2
    if n ==0 or n == 1 or n:
        return False
    elif n ==2:
        return True
    elif n ==3:
        return True
 
            
            
                
            