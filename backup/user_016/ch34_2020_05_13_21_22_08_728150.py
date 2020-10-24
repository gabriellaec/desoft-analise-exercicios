def eh_primo(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        if x%2 == 0:
            return False
        else:
            i = 3
            
            while i < x:
                if x%i == 0:
                    break
                i += 2
            if i == x:
                return True
            else:
                return False
def maior_primo_menor_que(n):
    lista = []
    i = 0
    while i <= n:
        if eh_primo(i) == True:
            lista.append(i)
        else:
            pass
        i += 1
        return lista[-1]