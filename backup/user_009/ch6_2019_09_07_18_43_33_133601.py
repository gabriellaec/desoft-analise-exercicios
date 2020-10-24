def encontra_maximo(m):
    max = 0
    for num in m:
        for num1 in num:
            if abs(num1) > abs(max):
                max = abs(num1)
    return max
        