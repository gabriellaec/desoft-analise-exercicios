def maior_primo_menor_que(n):
    while n > 0:
        x = n - 1
        while n % x != 0:
            if x == 2:
                return n
            x = x - 1
        n = n - 1
    return -1