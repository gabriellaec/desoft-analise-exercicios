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
def maior_primo_menor_que(N):
    # Casos não primos
    if N <= 1:
        resultado = -1
    else:
        # Se N é primo
        if verifica_primo(N):
            resultado = N
        else:
            # Verifica números que antecedem N um a um
            i = N-1
            while not verifica_primo(i):
                i -= 1
            resultado = i
    return resultado