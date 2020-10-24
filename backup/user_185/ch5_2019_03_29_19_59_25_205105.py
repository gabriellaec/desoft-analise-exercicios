def maior_primo_menor_que(n):
    i = 2
    while i<n:
        i = i + 1
        if n%i == 0:
            return False
    return -1
