def lista_primos(n):
    def eh_primo(x):
        if x == 2:
            return True
        elif x == 0 or x == 1:
            return False
        elif x%2 == 0:
            return False
        else:
            i = 3
            while i < x:
                if x%i == 0:
                    return False
                i = i+2
            return True
    lista = []
    i = 0
    x = 0
    while i < n:
        if eh_primo(x):
            lista.append(x)
            i = i + 1
        x = x + 1
    return lista
