def verifica_primo(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def maior_primo_menor_que(n):
    i = n
    while i >= 2:
        if verifica_primo(i):
            return i        
        i -= 1
    return -1
        