def eh_crescente(n):
    tamanho = len(n)
    i = 0
    if tamanho == 0:
        return False
    if tamanho > 0:
        while i < (tamanho - 1):
            if n[i+1] < n[i]:
                return False
            i = i + 1
    return True