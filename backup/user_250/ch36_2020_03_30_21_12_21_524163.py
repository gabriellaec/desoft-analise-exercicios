def fatorial(n):
    fat = n
    i = n - 1
    while i > 1:
        fat *= i
        i -= 1
    return fat
        