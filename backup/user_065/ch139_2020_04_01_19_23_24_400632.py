def arcotangente(x, n):
    result = x
    sqr = 3.0
    negative = 1
    for k in range(n):
        if negative is 0:
            result += (result**sqr)/sqr
            negative = 1
            continue

        if negative is 1:
            result -= (result**sqr)/sqr
            negative = 0
            continue
        sqr += 2
        n += 1
    return result