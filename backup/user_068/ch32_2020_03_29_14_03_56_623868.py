
def eh_primo(n):
    i = 2
    if n<=1:
        return False
    while i < n:
        if n % i != 0 or n == 2:
            return True
    return True

def lista_primos(n):
    a = 0
    lista = []
    i = 2
    while a < n:
        if eh_primo(i):
            lista.append(i)
            a += 1
        i += 1
    return lista
