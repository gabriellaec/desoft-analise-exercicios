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
    

def primos_entre(a,b):
    lista = []
    for i in range(a,b+1):
        if eh_primo(i) == True:
            if i > 0:
                lista.append(i)
    return lista