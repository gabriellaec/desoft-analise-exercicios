# Identifica se é primo ou não
def verifica_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n < 0: 
        return False
    else:
        for numero in range(3, n):
            if n %2 == 0:
                return False
            elif n %numero == 0:
                return False
        return True

# Define função
def primos_entre(a, b):
    lista_primos = []
    for numero in range(a, b+1):
        if verifica_primo(numero):
            lista_primos.append(numero)
    return lista_primos