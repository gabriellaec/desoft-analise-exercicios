
def eh_primo(numero):
    Primo = True
    n = 2
    if numero == 2 or numero != 0 or numero != 1 or numero%2 != 0:
        
        while numero%n != 0:
            n += 1
            if n == numero:
                Primo = True
            else:
                Primo = False
        
    else:
        Primo = False
    
    return Primo      

           