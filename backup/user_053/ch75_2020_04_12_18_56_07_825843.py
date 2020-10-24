# Define função que verifica se é primo
def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n < 0:
        return False
    elif n == 2:
        return True
    else:
        # Se nenhum número até sqrt(n) divide n, então ele é primo
        i = 3
        while i < n:
            if n %i == 0:
                return False
            elif n %2 == 0:
                return False
            i += 2
        return True

# Define função de verificação
def verifica_primos(lista):
    verificacao = {}
    # Varre e verifica números da lista
    for numero in lista:
        if eh_primo(numero):
            verificacao[numero] = True
        else:
            verificacao[numero] = False
    return verificacao