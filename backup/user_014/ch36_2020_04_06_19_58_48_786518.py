def fatorial (n):
    fat = 1
    for fat in range(n-1):
        fat = fat * n
        n = n - 1
    return fat