def check_primo(N):
    if N > 1:
        if N == 2:
            return True
        if N % 3 == 0:
            return False
        if N % 5 == 0:
            return False
        if N % 7 == 0:
            return False
        for i in range(2, N // 2):
            if (N % i) == 0:
                return False
            else:
                return True
    else:
        return False


def maior_primo_menor_que(n):
    lista_primos = []
    for i in range(2, n + 1):
        if check_primo(i) == True:
            lista_primos.append(i)
    if len(lista_primos) > 0:
        return lista_primos[len(lista_primos) - 1]
    else:
        return -1