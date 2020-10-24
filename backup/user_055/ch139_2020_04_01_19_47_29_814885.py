import math
def arcotangente(x, n):
    x = float()
    if x in range(-1,1):
        i = 1
        y = 1
        actan = [1]
        while len(actan) < n:
            ac = (x**i)/y
            actan.append(ac)
            i += 2
            y += 2
        soma = sum(actan)
        return math.degrees(soma)