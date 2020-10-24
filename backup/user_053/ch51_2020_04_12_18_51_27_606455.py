# Define função que verifica se é primo
def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
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
    for numero in lista:
        if eh_primo(numero):
            verificacao[numero] = 'É primo'
        else:
            verificacao[numero] = 'Não é primo'
    return verificacao