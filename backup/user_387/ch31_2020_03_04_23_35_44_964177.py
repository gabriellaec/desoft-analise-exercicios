import math

def eh_primo(n):
    n = math.sqrt(n**2)

    if n%2 == 0 and n != 2:
        return(False)
    
    else: 
        if n == 1 or n == 0:
            return(False)

        elif n == 2:
            return(True)
        
        else:
            a = 3
            while n != a:

                if n%a == 0:
                    return(False)
                    break

                else:
                    a+=2
            
            return(True)