def eh_primo(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        if n > 0:
            if n%2 == 0:
                return False
            else:
                impar = 3
                while impar < n:
                    if n%impar == 0:
                        return False
                    impar = impar + 2
                return True

def primos_entre(a,b):
    lista = []
    for i in range (a, b+1):
        if eh_primo(i) == True:
            lista.append(i)
    return lista