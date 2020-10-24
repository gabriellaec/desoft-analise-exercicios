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
    valor = 0
    if eh_primo(n) == True:
        return n
    elif n >= 0:
        for i in range(n+1):
            if eh_primo(i) == True:
                if i > valor:
                    valor = i
        return n
    else:
        return -1
    
print(maior_primo_menor_que(n))