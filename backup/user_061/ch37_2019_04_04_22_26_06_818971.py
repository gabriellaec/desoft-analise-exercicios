def eh_primo(p):
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    i = 3
    while i < p:
        if p % i == 0:
            return False
        i += 2
    return True
def imprime_primos(n):
    lista = []
    while f<=n:
        if eh_primo(i):
            lista.append(i)
            f+=f
    return lista