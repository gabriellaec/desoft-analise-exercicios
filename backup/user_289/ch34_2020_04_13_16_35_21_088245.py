def eh_primo (numero):
    if numero == 2:
        return True
    elif numero == 0 or numero == 1:
        return False
    elif numero%2 == 0:
        return False
    else:
        contador = 3
        while contador < numero:
            if numero%contador == 0:
                return False
            contador += 2   
        return True
def maior_primo_menor_que(n):
    if eh_primo(n) == True:
        return n
    i = n - 1
    while i < n:
        if eh_primo(i) == True:
            return i
        else:
            i -= 1
    return -1        
    