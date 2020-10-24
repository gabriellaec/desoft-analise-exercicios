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

def lista_primos(p):
    lista = [0]*p
    num = 3
    posicao = 1

    if p > 0:
        lista[0] = 2

        while posicao != p:

            if eh_primo(num) == True:

                lista[posicao] = num
                posicao += 1
                num += 2

            else:
                num += 2
            
        return(lista)

    else:
        return(lista)
        