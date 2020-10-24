def maior_primo_menor_que(n):
    if n == 2:
        return n
    if n == 1:
        return -1
    while n > 0:
        x = n - 1
        while n % x != 0:
            if x == 2:
                return n
            x = x - 1
        n = n - 1
    return -1