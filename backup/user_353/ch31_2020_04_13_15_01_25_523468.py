def eh_primo(x):
    if x == 2:
        return True
    elif x == 0 or x==1:
        return False
    elif x%2 == 0:
        return False
    else:
        contador = 3
        while contador < x:
            if x%contador == 0:
                return False
            contador += 2
        return True
        
        
    