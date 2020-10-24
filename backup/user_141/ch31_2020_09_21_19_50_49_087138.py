n = 2
def eh_primo(numero):
    if numero == 2 or numero != 0 or numero != 1 or numero%2 != 0:
        
        while numero%n != 0:
            n += 1
        if n == numero:
            numero = True
        else:
            numero = False
    
    
    else:
        numero = False
    
            
           

           