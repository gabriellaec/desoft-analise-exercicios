def collatz(n):
    elementos = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        terms += 1
    return terms


def maiorcollatz():
    j = 0
    i = 1
    while i < 1000:
        s = collatz(i)
        if s > j:
            j = s
            maior = i
        i += 1

    return maior


