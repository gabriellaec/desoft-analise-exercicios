def encontra_maximo(m):
    max = 0
    for num in m:
        for num1 in num:
            if num1 > max:
                max = num1
    return max
        