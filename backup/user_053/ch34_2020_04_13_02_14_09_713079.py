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
def maior_primo_menor_que(N):
    # Casos negativos
    if N <= 0:
        resultado = -1
    else:
        # Se N é primo
        if eh_primo(N):
            resultado = N
        else:
            # Verifica números que antecedem N um a um
            i = N
            while not eh_primo(i):
                i -= 1
            resultado = i
    return resultado