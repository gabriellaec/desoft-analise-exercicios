def eh_primo(p):
        if p == 0:
            return False
        elif p == 1:
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
def maior_primo_menor_que(n):
    i= 0
    lista = []
    while i <= n:
        if eh_primo(i):
            lista.append('i')
            