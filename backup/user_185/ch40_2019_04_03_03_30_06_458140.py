def fatorial(n):
    if n > 0:
        index = 1
        multiplicação = index
        while index <= n:
            multiplicação = multiplicação*index
            print(multiplicação)
            index = index + 1