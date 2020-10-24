def eh_primo(numero):
    if numero == 0 or numero == 1:
        return False
    elif numero == 2 or numero == 3:
        return True
    elif numero % 2 == 0:
        return False
    else:
        i = 3
        while numero > i:
            if numero % i == 0:
                return False
            else:
                i += 1
        if i >= numero:
            return True

def lista_primo(n):
    lista = []
    i = 0
    while len(lista) < n:
        if eh_primo(i):
            lista.append(i)
        i += 1
    return lista