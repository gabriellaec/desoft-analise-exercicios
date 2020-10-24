n = 2
def eh_primo(numero):
    if numero != 0 and numero != 1 and numero%2 != 0:
        n = numero
        while numero/n != 1:
            n += 1
    else:
        numero = False
    return n

            
           

           