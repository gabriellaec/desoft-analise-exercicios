i=1
def eh_primo(n):
    n=input('escolha um numero')
    if n%2==0 and n!=2:
        return True
    else:
        while i<n:
            if n%i==0:
                i+=2
                return True
            else:
                return False
            
    
            
           
                
            
            
        
        