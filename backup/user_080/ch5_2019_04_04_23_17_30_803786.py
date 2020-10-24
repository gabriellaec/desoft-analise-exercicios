def maior_primo_menor_que(n):
    start = 2;

    while start <= math.sqrt(n):
        if n % start < 1:
            return False;
        start += 1;

    return n > 1;