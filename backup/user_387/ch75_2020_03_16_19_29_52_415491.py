def eh_primo(n):

    if n%2 == 0 and n != 2:
        return(False)
    
    else: 
        if n <= 1:
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

def verifica_primos(a):
    primos = {}
    for number in a:
        primos[number] = eh_primo(number) 
    return primos
