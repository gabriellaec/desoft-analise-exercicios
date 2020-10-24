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
def primos_entre(a,b):
    lista = []
    for i in range(a,b+1):
        if eh_primo(i) == True:
            lista.append(i)
        else:
            pass
    return len(lista)