import math
def arcotangente(x, n):
    x = float()
    if x in range(-1,1):
        i = 1
        y = 1
        x = 1
        actan = [1]
        while len(actan) < n:
            ac = ((x**i)/y) * x
            actan.append(ac)
            i += 2
            y += 2
            x *= 1
        soma = sum(actan)
        return math.radians(soma)