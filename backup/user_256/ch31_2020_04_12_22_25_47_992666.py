def eh_primo(n):
    i = 1
    if n ==0 or n == 1:
        return False
    if n ==2:
        return True
    while n>2 and i<n:
        while n %2 !=0:
            if n%i !=0:
                return True
            else:
                return False
         
        i+=2
            
            
                
            