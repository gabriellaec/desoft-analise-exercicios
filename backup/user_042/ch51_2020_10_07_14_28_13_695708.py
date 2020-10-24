def eh_primo(p):
        if p == 0:
            return False
        elif p == 1:
            return False
        if p < 0:
            return False
        if p == 2:
            return True
        elif p % 2 ==0:
            return False
        impares = 3
        while impares < p:
            if p % impares == 0:
                return False
            impares += 2
        return True
def primos_entre(a,b):
    lista_primos = []
    quantidade = 0
    p = a
    while p <= b:
        if eh_primo(p):
            lista_primos.append(p)
            quantidade += 1
        p += 1
    return lista_primos