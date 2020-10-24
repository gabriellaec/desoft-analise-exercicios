n = 2
def eh_primo(numero):
    if numero != 0 and numero != 1 and numero%2 != 0:
        
        while numero%n != 0:
            n += 1
        if numero == n:
            numero = True
    
    elif numero == 2:
        numero = True
           
    else:
        numero = False
    return numero

            
           

           