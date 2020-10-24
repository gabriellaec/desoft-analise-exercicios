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
  
def maior_primo_menor_que(n):
    a=0
    b=n-1
    if n<=1:
        return -1
    while a>n:
        if eh_primo(b):
        	return b
        a+=1
        b-=1
        
    
