def primos_entre(a, b):
    def eh_primo(x):
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        elif x == 0 or x == 1:
            return False
        else:
            i = 3
            while i < x:
                if x % i == 0:
                    return False
                i = i + 1
            return True
    lista = []
    x = a
    while a<= x <=b:
        if eh_primo(x):
            lista.append(x)
        x = x + 1
    return lista