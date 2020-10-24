
def lista_de_primos(n):
    m=0
    primos = []
    while m<=n:
        if print(eh_primo(m))=='True':
            primos.append(m)
            m=m+1
    return primos
    