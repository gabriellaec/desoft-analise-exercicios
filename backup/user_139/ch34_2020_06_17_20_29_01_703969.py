def eh_primo (n):
    if n == 2:
        return True
    elif n == 0 or n == 1 or n %2 == 0:
        return False
    i = 3
    while i < n:
        if n % i == 0:
            return False
        else: 
            i += 2

    return True

def maior_primo_menor_que (n):
    i = 0
    numero = 0
    while i < n + 1:
        if eh_primo(i) == True:
            numero = i
            i += 1
        else:
            i += 1
            numero = -1
    return numero