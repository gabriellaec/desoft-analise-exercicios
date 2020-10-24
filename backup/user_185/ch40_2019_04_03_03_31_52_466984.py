def fatorial(n):
    if n > 0:
        index = 1
        multiplicação = index
        while index <= n:
            multiplicação = multiplicação*index
            index = index + 1
    return multiplicação