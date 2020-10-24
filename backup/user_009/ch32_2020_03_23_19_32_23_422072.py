def eh_primo(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x%2 == 0:
        return False
    else:
        n = 3
        while n < x:
            if x%n == 0:
                return False
            n += 2
        return True

def lista_primos(lista):
    lista1 = []
    for i in lista:
        eh_primo(i)
        if eh_primo(i) == True:
        	lista1.append(i)
    return lista1