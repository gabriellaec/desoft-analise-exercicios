def eh_primo (n):
    if n==2:
        return True
    if n==0 or n==1:
        return False
    i=2
    while  i<n:
        if n % i == 0:
        	return False 
        i = i+1
    return True 

def imprime_primos (x):
    i=0
    while i<=x:
        if eh_primo(i) == True:
            print (i)
        i = i+1   
            
        
    