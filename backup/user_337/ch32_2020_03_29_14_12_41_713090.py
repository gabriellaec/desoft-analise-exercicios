def eh_primo(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        if n%2 == 0:
            return False
        else:
            impar = 3
            while impar < n:
                if n%impar == 0:
                    return False
                impar = impar + 2
            return True

def lista_primos(n):
    lista = []
    primo = 0
    while len(lista)<= n:
        while eh_primo(primo) == False:
            primo += 1
        lista.append(primo)
        primo += 1
    return lista