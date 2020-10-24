def eh_primo(numero):
    if numero == 0 or numero == 1:
        return False
    elif numero == 2:
        return True
    elif numero%2 == 0:
        return False
    else:
        x = 3
        while x < numero:
            if numero%x != 0:
                x += 2
            else:
                return False
        return True
    

def lista_primos(n):
    lista = [2]*n
    x = 3
    i = 2
    while i < n+1:
        if eh_primo(x):            
            lista[i-1] = x
            i += 1
        x += 2    
    return lista