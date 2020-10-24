def eh_primo (n):
    if n == 2:
        return True
    elif n == 0 or n == 1:
        return False
    elif n%2 == 0:
        return False
    else:
        contador = 3
        while contador < n:
            if n%contador == 0:
                return False
            contador += 2    
        return True
def maior_primo_menor_que(q):
    contador=q
    while contador >0:
        if eh_primo(q)==True:
            return q
            contador=0
        else:
            q-=1
    return -1