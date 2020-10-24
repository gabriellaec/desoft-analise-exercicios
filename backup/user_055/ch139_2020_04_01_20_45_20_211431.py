import math
def arcotangente(x, n):
    x = float()
    if x in range(-1,1):
        i = 1
        y = 1
        b = 1
        actan = [1]
        while len(actan) < n:
            ac = math.radians(((x**i)/y) * b)
            actan.append(ac)
            i += 2
            y += 2
            b *= (-1)
        soma = sum(actan)
        return soma