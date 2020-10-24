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

def maior_primo_menor_que(n):
    maior = -1
    resultado = 0
    for i in range(n):
        if eh_primo(i) == True:
            if i <= n:
                n = i
            else:
                n = -1
    return n