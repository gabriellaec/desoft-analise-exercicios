def eh_crescente(n):
    tamanho = len(n)
    i = 0
    while i < (tamanho - 1):
        if n[i+1] > n[i]:
            return True
        else:
            return False
        i = i + 1