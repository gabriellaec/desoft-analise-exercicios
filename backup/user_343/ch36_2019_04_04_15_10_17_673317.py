def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        y=n%2
        while y>=0:
            y=n%2
            if y==0:
                return False
            else:
                return True
print (eh_primo(n))            

        
    
   
