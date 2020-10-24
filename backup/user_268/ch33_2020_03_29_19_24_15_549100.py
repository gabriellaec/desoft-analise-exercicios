def eh_primo(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
def primos_entre(a,b):
    c=0
    p=0
    while p<b:
        p+=1
        if eh_primo(p) and a<=p<=b:
            c+=1
    return c
        
        
        
    
    
    
    
    