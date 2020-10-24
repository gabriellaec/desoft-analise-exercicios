def raiz_quadrada (n):
    i = 1
    count = 0
    while n >= i:
        n = n - i
        i = i + 2
        count = count + 1
    return count