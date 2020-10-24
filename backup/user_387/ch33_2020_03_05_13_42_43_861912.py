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
                    n = 5
                    a = 4
                   
                    return(False)
             
                else:
                    a+=2
            
            return(True)


def primos_entre(a,b):

    p = 0

    for ele in range((a+1),b):

        if eh_primo(ele) == True:
            p+=1

    return(p)
