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

def maior_primo_menor_que(n):

    if n <= 1:
        return(-1)

    else:
        while eh_primo(n) != True:
             n-=1

        return(n)


print(maior_primo_menor_que(1))
