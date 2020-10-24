# Identifica primos
def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n < 0:
        return False
    else:
        i = 3
        while i < n:
            if n %i == 0:
                return False
            elif n %2 == 0:
                return False
            i += 2
        return True

# Define função
def primos_entre(a, b):
    lista_primos = []
    for numero in range (a, b + 1):
        if eh_primo(numero):
            lista_primos.append(numero)
    return len(lista_primos)