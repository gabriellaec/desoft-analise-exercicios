
i=1
def eh_primo(n):
    if n%2==0:
        if n==2:
            return True
        else:
            while i<n:
                if n%i==0:
                    return False
                else:
                    i+=2
    elif n==0 or n==1:
        return False
    else:
        return True
   
          
           
      
    