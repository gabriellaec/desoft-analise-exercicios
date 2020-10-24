def eh_primo(n):
    i = 3
    if n ==0 or n == 1 or n:
        return False
    if n ==2 or n==3:
        return True
    while n>3 and i<n:
        while n %2 !=0:
            if n%i !=0:
                return True
            else:
                return False
        else:
            return False
         
        i+=2
            
            
                
            