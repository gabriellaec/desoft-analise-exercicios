def fatorial (n):
    fat = 1
    for i in range(n):
        fat = fat * n
        n = n - 1
    return fat